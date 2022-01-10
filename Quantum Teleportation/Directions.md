In this module you will teleport the state information from the first qubit
(q0) to the third qubit (q2), and then validate the state on q2. The learning objective of this module is to learn the quantum teleportation protocol and to further explore how to make use of entanglement phenomena in quantum computing.

Import the following libraries:
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.extensions import Initialize
from qiskit.quantum_info import random_statevector
from qiskit.ignis.verification import marginal_counts

Begin by creating a 3-qubit register and applying a Pauli X-gate to q0.

From our circuit we can tell that if we measured each qubit now then q0 would
be in state |1⟩, while q1 & q2 would both be in state |0⟩. Now, apply a
Hadamard gate to q1 and a CX gate to entangle q1 and q2.

Next, entangle q0 and q1, and then apply a Hadamard gate to q0.

Predict the outcome of a measurement on q0 and q1 using Dirac notation, and
then measure q0 and q1.

Now, entangle q1 and q2 with a CX gate, and then a CZ gate between q0 and q2. Consider what the purpose of the measurement step is, noting that only q2
remains in an unknown state.

Finally, measure q2, choose a reasonable number of shots, and create a
histogram of the counts.

Do these results make sense? Explain why this is not a violation of the
no-cloning theorem. We have successfully teleported the information from q0 to  
q2 if c2 reads as |1⟩ (=X|0⟩). In the histogram, q0, q1, and q2 are blue, red,
and purple, respectively.

The following is optional, and is the same procedure running on a quantum computer. You will need a token from IBM Quantum to run this part of the code.

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

What is the difference between this result and that of the simulation, and why?
