The hallmark of this algorithm is the oracle. Let's think about how to setup an oracle to let us know whether the function is constant. We do this via entanglement, which can be achieved through the straightforward application of CX gates with the Hadamards. If the function is constant, the input should not effect the output, so you will want to make the results the same, which can be achieved via an X gate. If the function is balanced, you'll apply an X gate to the 1 digits, then a CX to all the qubits with the last qubit as the target, followed by another X gate on the same qubits you assigned them to before. This ensures that all the qubits are entangled with the target qubit.

Import the following libraries:
import numpy as np
from qiskit import *
from qiskit.tools.visualization import plot_histogram

Start by defining a function called oracle that takes the integer n as a parameter. In the function create an n+1 qubit circuit. Then create an if-elif statement that checks to see if the function is constant or balanced. Include an option for a random choice between the two cases. When the function is constant, choose whether you want to output all 0 or 1 and enforce the condition.

If the function is balanced generate a binary number of n characters. iterate over that binary number and if a digit is 1, perform an X gate operation on the corresponding qubit. Then apply a CX to each qubit except the last one and use the last qubit as the target for each CX. Finally, apply an X gate to the same qubits you did previously.

The function should return the oracle as a gate.

Now, let's build a circuit that uses the oracle. The circuit should have n+1 qubits and n classical bits. We will call q0 through qn−1 input qubits and qn
the output qubit. Apply Hadamards to all the input qubits, and XH to the output qubit. What are the states of each qubit currently?

Add the oracle you defined earlier to the circuit, apply Hadamards to each input qubit, and then measure the input qubits.

Does this result make sense? Consider what the oracle is doing to an input qubit and the purpose of the inclusion of the Hadamard before measurement.

Optionally, run this program on the quantum computer.

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
