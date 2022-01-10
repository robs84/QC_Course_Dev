from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.extensions import Initialize
from qiskit.quantum_info import random_statevector
from qiskit.ignis.verification import marginal_counts

#Generating and visualizing a three qubit register with a NOT gate on the first qubit
circuit = QuantumCircuit(3, 3)
psi = random_statevector(2)
init_gate = Initialize(psi)
circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')

#Generating a Hadamard and CNOT on the second and third qubits, creating entanglement between the two
circuit.h(1)
circuit.cx(1,2)
circuit.draw(output='mpl')

#Entangling the first and second qubits
circuit.cx(0,1)
circuit.h(0)
circuit.draw(output='mpl')

#Measuring with the first and second qubits with the classical register
circuit.barrier()
circuit.measure([0,1], [0,1])
circuit.draw(output='mpl')

#CNOT on qubits two and three, and a CZ on qubits one and three
circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw(output='mpl')

#circuit.append(init_gate.gates_to_uncompute(), [2])
circuit.measure(2,2)
circuit.draw(output='mpl')

simulator = Aer.get_backend('qasm_simulator')
#result = execute(circuit, backend = simulator, shots = 1000).result()
#counts = result.get_counts()
#plot_histogram(counts)
t_qc = transpile(circuit, simulator)
t_qc.save_statevector()
counts = simulator.run(t_qc).result().get_counts()
qubit_counts = [marginal_counts(counts, [qubit]) for qubit in range(3)]
plot_histogram(qubit_counts)

from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy

IBMQ.load_account()
IBMQ.providers()

provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                   not b.configuration().simulator and b.status().operational==True))
t_qc = transpile(circuit, backend, optimization_level=3)
job = backend.run(t_qc)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)
qubit_counts = [marginal_counts(counts, [qubit]) for qubit in range(3)]
plot_histogram(qubit_counts)
