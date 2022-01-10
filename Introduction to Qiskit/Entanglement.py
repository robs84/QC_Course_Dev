from qiskit import *
from qiskit.tools.visualization import plot_histogram

#the quantum register we will be operating on and the classical register to measure with
qr = QuantumRegister(2)
cr = ClassicalRegister(2)

#the circuit that is composed of both the quantum and classical register
circ1 = QuantumCircuit(qr,cr)

'''
Adding a Hadamard gate to the circuit. Recall that the Hadamard tapplied to a single qubit
of a given state outputs a normalized linear superposition of states in that
(computational or +/-) basis.
'''
circ1.h(qr[0])
circ1.draw(output = 'mpl')

#a CNOT gate entangles the two qubits in our quantum register
circ1.cx(qr[0],qr[1])
circ1.measure(qr,cr)
simulator = Aer.get_backend('qasm_simulator')
result1 = execute(circ1, backend = simulator).result()
circ1.draw(output = 'mpl')

circuit2 = QuantumCircuit(qr,cr)
circuit2.h(qr[0])
circuit2.h(qr[0])
circuit2.cx(qr[0],qr[1])
circuit2.measure(qr,cr)
result2 = execute(circuit2, backend = simulator).result()
circuit2.draw(output = 'mpl')

plot_histogram(result2.get_counts(circuit2)) #100% in the |00> state

circuit3 = QuantumCircuit(qr,cr)
circuit3.h(qr[0])
circuit3.cx(qr[0],qr[1])
circuit3.h(qr[0])
circuit3.measure(qr,cr)
result3 = execute(circuit3, backend = simulator).result()
circuit3.draw(output = 'mpl')

plot_histogram(result3.get_counts(circuit3))#approximately evenly divided among the four states
