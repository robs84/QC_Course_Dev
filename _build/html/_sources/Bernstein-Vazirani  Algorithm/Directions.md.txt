Import the following libraries:
from qiskit import *
from qiskit.tools.visualization import plot_histogram

Begin by defining a binary string that will serve as your secret number. The string can be however long as you like.

Now, build a general quantum circuit that contains the same number of qubits as the number of digits your secret number has, and an equal number of classical bits. Apply Hadamard gates to all but the last qubit. Apply an X gate and then
a Hadamard gate to the last qubit in your register. Consider what function the
HX serves.

Next, create a for loop to entangle your last qubit to only those qubits that
are measuring a 1 on the secret number. What would happened if you entangled
all the other qubits to the last qubit instead of just the ones measuring 1?

Finally, apply Hadamard gates to all but the last qubit and measure all bit the last qubit

Run the simulation with only 1 shot. Was the guess correct?

Optionally, run this algorithm on a quantum computer. Try 1, 10, 100, and 1000 shots. What if anything changes? Note: it is best to keep your secret number to four digits or less to stay within the quantum computer's open resource
allocation.

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
