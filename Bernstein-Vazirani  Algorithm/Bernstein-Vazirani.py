from qiskit import *
from qiskit.tools.visualization import plot_histogram

#chose a secret number
secretnumber = '1010'

#building a quantum circuit with the number of qubits equal to the number of bitwise digits in the secret number
circuit = QuantumCircuit(len(secretnumber)+1, len(secretnumber))
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))
circuit.barrier()

#CNOT is applied to those digits that are a 1, analogous to the AND operator in classical computing
for ii, yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit.cx(ii, len(secretnumber))
circuit.barrier()
circuit.h(range(len(secretnumber)))

#measuring
circuit.measure(range(len(secretnumber)), range(len(secretnumber)))
circuit.draw(output='mpl')

#using the backend to simulate this circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts)

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
