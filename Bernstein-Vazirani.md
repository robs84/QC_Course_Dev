# Bernstein-Vazirani
******************

 Numbers can be stored as bits, just as any character can.  For integers, the conversion to binary involves dividing by two and recording the remainder.  The remainder values are written in reverse order, or right to left.  For example, the number 45 can be stored as the six-digit bitwise number 101101.
   Consider a box and we store a bit-wise number inside.  The box is only accessible via an oracle.  If we make a guess at one or more digits of the number stored within, the oracle will reveal whether we guessed correctly or not.  The oracle will not reveal full details about the number directly, nor can we see inside the box.  Only by guessing correctly will the number be revealed.  Naively, we could start with zero and guess every permutation of ones and zeroes until we get the right answer.  
   Perhaps a more strategic response on a classical computer would be to use the AND operation to bit-wise solve for the full number.  An AND operation is simply when the compared bit is a 1 it returns a 1, otherwise it returns a 0.  Using this method each bit only needs to be tested once, so to resolve the secret N-digit bit-wise number we would need N attempts.  For example, this method would reveal our binary 45 in six attempts.  In quantum computing, application of the Bernstein-Vazirani algorithm can successfully guess the secret number in just 1 attempt through qubit entanglement, regardless of the size of the bit-wise number.  Details about the Bernstein-Vazirani algorithm can be found in the following reference: 

   Ethan Bernstein and Umesh Vazirani (1997) "Quantum Complexity Theory" SIAM Journal on Computing, Vol. 26, No. 5: 1411-1473, doi:10.1137/S0097539796300921.

---

Import the following libraries:

	from qiskit import *
	from qiskit.tools.visualization import plot_histogram

- Begin by defining a binary string that will serve as your secret number. The string can be however long as you like.

- Now, build a general quantum circuit that contains the same number of qubits as the number of digits your secret number has, and an equal number of classical bits. Apply Hadamard gates to all but the last qubit. Apply an X gate and then
a Hadamard gate to the last qubit in your register. Consider what function the
HX serves.

- Next, create a for loop to entangle your last qubit to only those qubits that
are measuring a 1 on the secret number. What would happened if you entangled
all the other qubits to the last qubit instead of just the ones measuring 1?

- Finally, apply Hadamard gates to all but the last qubit and measure all bit the last qubit

- Run the simulation with only 1 shot. Was the guess correct?

- Optionally, run this algorithm on a quantum computer. Try 1, 10, 100, and 1000 shots. What if anything changes? Note: it is best to keep your secret number to four digits or less to stay within the quantum computer's open resource
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
