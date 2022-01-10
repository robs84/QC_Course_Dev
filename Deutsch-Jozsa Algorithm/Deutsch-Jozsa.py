import numpy as np
from qiskit import *
from qiskit.tools.visualization import plot_histogram

n = 4

def oracle(n):
    #create the oracle
    oracle = QuantumCircuit(n+1)
    #randomly pick 0 or 1
    value = np.random.randint(2)
    #the random assignment of a case
    #if case == 'random':
        #value = np.random.randint(2)
    if value == 1:
            #case = 'constant'
        number = np.random.randint(2)
        if number == 1:
            oracle.x(n)
        print('constant function')
    else:
            #case = 'balanced'
        #generate the binary string
        binary = np.random.randint(1,2**n)
        binary_str = format(binary, '0'+str(n)+'b')
        #iterate over the binary string and apply an X gate whenever there's a 1, otherwise do nothing
        for qubit in range(len(binary_str)):
            if binary_str[qubit] == '1':
                oracle.x(qubit)
        #apply CX to qubits-0 to n-1, with qubit-n as the target
        for qubit in range(n):
            oracle.cx(qubit, n)
        #apply X gates to the same qubits as before
        for qubit in range(len(binary_str)):
            if binary_str[qubit] == '1':
                oracle.x(qubit)
        print('balanced function')


    gate = oracle.to_gate()
    return gate

circuit = QuantumCircuit(n+1, n)
#apply Hadamards to the input qubits
for qubit in range(n):
    circuit.h(qubit)
#apply HX to the output qubit
circuit.x(n)
circuit.h(n)
circuit.barrier()

#append the oracle gate to the circuit
circuit.append(oracle(n), range(n+1))
#apply Hadamards to all the input qubits
for qubit in range(n):
    circuit.h(qubit)
circuit.barrier()
#measure the input qubits
for i in range(n):
    circuit.measure(i, i)
circuit.draw(output='mpl')

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
plot_histogram(counts)

from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy

IBMQ.load_account()
IBMQ.providers()

provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                   not b.configuration().simulator and b.status().operational==True))
t_qc = transpile(circuit, backend)
job = backend.run(t_qc, shots = 1000)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)
plot_histogram(counts)
