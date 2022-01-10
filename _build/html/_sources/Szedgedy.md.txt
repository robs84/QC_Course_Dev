# Szedgedy
********

Previously in this course, you explored a quantum Monte Carlo application of an Ising model.  An Ising model is generally known to be a Markov random field and has been used to model many physical systems and interesting problems (modeling ferromagnetics, phase transitions, step-growth of a polymer chain, etc.).  A Markov process can be viewed as a random walk where each step is only contingent upon the previous step but is otherwise random.  In this module we will use the phenomenon of superposition (taking all allowed steps at once) to quadratically increase the speed to locate a marked lattice point for a random walk on a 4-dimensional hypercube where each vertex is connected only to its nearest neighbors.  To realize this quantum walk we will implement an algorithm based on the works of Szegedy and Wong.  Szegedy formally introduced the problem speed-up of a Markov process using a quantum algorithm and Wong showed the equivalency of Szegedy's quantum walk to a Markov process that uses part of Grover's algorithm to generate the superposition needed for the quadratic speed-up.  Alternatively, you can use the Hadamard gate to develop the desired superposition.  This exercise is adapted from the Qiskit textbook, so if you get stuck you can look here: https://qiskit.org/textbook/ch-algorithms/quantum-walk-search-algorithm.html

More information about the use of Grover's algorithm in a quantum walk protocol can be found in the following references:

M. Szegedy, Quantum speed-up of Markov chain based algorithms, in45th Annual IEEE Symposium on Foundations of Computer Science, Proceedings, IEEE Comp Soc, Tech Soc Fdn Comp (IEEE COM-PUTER SOC, 2004) pp. 32–41.

T. G. Wong, Equivalence of Szegedy’s and coined quantum walks, Quantum Inf. Process., 10.1007/s11128-017-1667-y (2017).

---

In this module, we will use a coin walk (as in flip a coin to determine which direction to move). If we used a Hadamard to produce our superposition state
among all qubits, then the coin would determine the movement from lattice site
to lattice site. Instead we will use use the diffusion component of Grover's algorithm that allowed for an efficient search protocol to generate the desired superposition. The coin state can be visualized as a vector in Hilbert space.
The algorithm requires an update to the position state vector, which is
achieved through a shift operator.

Import the following libraries:

	from qiskit import *
	from qiskit.visualization import *
	from matplotlib import pyplot as plt
	import numpy as np

The algorithm we will employ has three main steps: setup the initial
superposition over the edges, reflect over any bad states and the current state until the marked states is reached, and measurement in the computational basis. The number of reflections needed is O(√(N/|M|)) where M is the set of marked vertices and N is the total number of vertices. For a 4D hypercube (tesseract) what is the value of N? The initial state can be written as an arbitrary superposition of marked (m) and unmarked (u) states, x=sinθ|m⟩+cosθ|u⟩, where
θ=√(|M|/N).

There are two primary components to this circuit, a phase oracle and a phase estimation. The oracle notes the marked state, and as such indicates the states
to phase shift over. This is analogous to the state amplification Grover's algorithm uses. The phase estimation updates the "walker" or state that
occupied at the current step. The phase estimation ensures that the evolution
is always orthogonal to the previous state and is achieved via the rotation of
an auxiliary qubit.

- First, we want to build a phase oracle gate. This will be a 6-qubit quantum register that defines the target state(s). For now, let's choose just one state. Assign |1111⟩ as the quantum walk target state. To do this apply a Hadamard to
𝑞3, followed by a multi-controlled X gate (mct in Qiskit) to entangle 𝑞0 through 𝑞2 to 𝑞3, and then apply another Hadamard to 𝑞3.

- Next, we will begin to assemble the phase estimation gate. Let's begin by
defining some functions that will be used to build the circuit. Start with a quantum Fourier transform (QFT) as you did in Shor's algorithm.

- Then, define both the QFT where n =4 and its inverse. This is easy enough using the inverse() attribute.

- Next, define a function that shifts the walker to the new step on our tesseract (we will end up using six qubits for this system). You can achieve this using a for loop to iterate over q0 through q3 and apply a CCX gate, which entangles
three qubits, to that qubit, q4, and q5. Then, before moving to the next qubit, apply an X gate to q4. Also apply an X gate to q5 under the modulo two
condition (i.e. q%2 == 0).

- Build a circuit that consists of a 5-qubit quantum register. The function
should rotate q4 whenever any other qubit is non-zero. To do this, apply an X
gate to each qubit. Then, apply a multi-controlled X gate to entangle q0
through q3 to q4. Apply a Z gate to q4, then repeat the multi-controlled X gate followed by the X gates, as before.

- Now, continue by generating a 6-qubit quantum register. Then, to q4 and q5
apply a ZH. What is the state of the two qubits? Apply CZ to q4 and q5,
followed by a Hadamard on both qubits. This series of gates determines the direction of the step, and is generally referred to as the coin.

- Append the circuit to include the shift gate and then also take the inverse the circuit. We need to take the inverse of the circuit to reverse the phase estimation we will be generating soon. We will call this entire circuit the
step gate and inverse step gate.

- Now, we want both the step and inverse step gates to be control gates. This is simply done in Qiskit using the control() attribute.

- The final component of the phase estimation portion of the circuit is to
assemble it from the components we developed. This will be an 11 qubit circuit.
To do that we first need to apply a Hadamard gate to the first four qubits.
Then, use a nested for loop to iterate over the vertices and append the circuit with the step gate where the 6 qubits are q4 through q9 and the control as the current qubit being acted on. Next, append the circuit to apply the inverse QFT
to q0 through q3. Then append the circuit to add the check circuit where the 5 qubits are q0 through q3 and q10 (instead of q4). Can you reason through how
this phase estimation works?

- Now we will reverse the phase estimation. Append the circuit to apply the QFT
to q0 through q3. Then repeat the nested for loop from before, but going
backwards (q3 to q0) and applying the controlled inverse step gate. Finally,
apply Hadamards to the first four qubits.

- Now, to implement the quantum walk build a circuit with an 11-qubit quantum register and a 4-bit classical register. Apply Hadamards to q4 through q9,
which establishes our initial superposition state. Apply the phase oracle to q4 through q9 followed by the phase estimation to all qubits. Again, apply the
phase oracle and phase estimation three more times, making a total of four iterations of repeating phase oracle followed by phase estimation gates.
Complete the circuit by measuring q4 through q7. We chose to work with a
tesseract with one marked vertex, so four iterations is the expected to demonstrate this algorithm based on the information above; however, in practice
we can use less and get a reasonable outcome. 

- Next, simulate your quantum walk and plot a histogram of your counts after 1000 shots. What are your results? Consider using 2, 3, 4, 5, and 6 iterations and observe the change in the histogram at the end of this module. Can you reason
why the number of iterations that yield the best result is 3 instead of 4?  
Hint:  the answer can be found in the literature provided in the README file.  

- Try this exercise with a second target state, and then with three target states. Depending on your choice of target states, your phase oracle will require additional gates but the phase estimation will remain unchanged. The number of iterations needed will decrease with increasing number of target states.
