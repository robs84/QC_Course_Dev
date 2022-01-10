from qiskit import *
from qiskit.visualization import *
from matplotlib import pyplot as plt
import numpy as np

phase_gate =  QuantumCircuit(6, name='oracle')
# mark 1111
phase_gate.h(3)
phase_gate.mct([0,1,2],3)
phase_gate.h(3)
phase_gate.draw("mpl")

# QFT gate
def qft(n):
    qft = QuantumCircuit(n)
    for qubit in range(n//2):
        qft.swap(qubit, n-qubit-1)
    for i in range(n):
        for k in range(i):
            qft.cp(-np.pi/float(2**(i-k)), k, i)
        qft.h(i)
    qft.name = "QFT"
    return qft

qft_circ = qft(4)
inv_qft = qft_circ.inverse()

# shift operator function
def shift(circuit):
    for q in range(0,4):
        circuit.x(4)
        if q%2==0:
            circuit.x(5)
        circuit.ccx(4,5,q)

check_circuit = QuantumCircuit(5, name='rotate')
check_circuit.x([0,1,2,3,4])
check_circuit.mct([0,1,2,3], 4)
check_circuit.z(4)
check_circuit.mct([0,1,2,3], 4)
check_circuit.x([0,1,2,3,4])
check_circuit.draw("mpl")

coin_circuit = QuantumCircuit(6, name = 'circuit')
coin_circuit.h([4,5])
coin_circuit.z([4,5])
coin_circuit.cz(4,5)
coin_circuit.h([4,5])
coin_circuit.draw("mpl")

shift(coin_circuit)
step_gate = coin_circuit
step_gate.draw("mpl")
inv_step_gate = coin_circuit.inverse()
inv_step_gate.draw("mpl")

control_step = step_gate.control()
control_inv_step = inv_step_gate.control()

# phase estimation
pe_gate = QuantumCircuit(11, name='phase estimation')
pe_gate.h([0,1,2,3])
for i in range(0,4):
    end = 2**i
    for j in range(0,end):
        pe_gate.append(control_step, [i,4,5,6,7,8,9])
pe_gate.append(inv_qft, [0,1,2,3])
pe_gate.append(check_circuit, [0,1,2,3,10])

# Reverse phase estimation
pe_gate.append(qft_circ, [0,1,2,3])
for k in range(3,-1,-1):
    end = 2**k
    for l in range(0,end):
        pe_gate.append(control_inv_step, [k,4,5,6,7,8,9])
pe_gate.barrier(range(0,10))
pe_gate.h([0,1,2,3])
pe_gate.draw("mpl")

circuit = QuantumCircuit(11,4)
# Apply Hadamard gates to generate the initial superposition state
circuit.h([4,5,6,7,8,9])
circuit.append(phase_gate, [4,5,6,7,8,9])
circuit.append(pe_gate, [0,1,2,3,4,5,6,7,8,9,10])
circuit.append(phase_gate, [4,5,6,7,8,9])
circuit.append(pe_gate, [0,1,2,3,4,5,6,7,8,9,10])
circuit.append(phase_gate, [4,5,6,7,8,9])
circuit.append(pe_gate, [0,1,2,3,4,5,6,7,8,9,10])

# measure the final walker state
circuit.measure([4], [0])
circuit.measure([5], [1])
circuit.measure([6], [2])
circuit.measure([7], [3])
circuit.draw("mpl")

backend = Aer.get_backend('qasm_simulator')
job = execute( circuit, backend, shots=1000)
count = job.result().get_counts()
plot_histogram(count)
