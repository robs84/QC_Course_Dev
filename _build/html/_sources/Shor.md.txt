# Shor
****

The current standard algorithm for encryption is RSA.  RSA relies in the challenge of factoring very large composite which are numbers whose factors are prime numbers.  Factoring composite numbers is a problem that requires greater than polynomial time to resolve using a classical computer.  Factoring can be mapped into a period finding problem.  In this problem, the periodic function ($f(x) = f(x+r)$) has a unique solution for each input, the number of arguments ($N$) can be divided by the period ($r$) without a remainder, and that the number of periods is larger than the period itself ($\frac{N}{r} >> r$).  This can be a hard problem when M is very large.  Shor's algorithm is a quantum algorithm that is able to find the period (and thereby factorize) in polynomial time, which is a considerable improvement over anything a classical computer can do.  In this module you will be guided in implementing a very Shor's algorithm in Qiskit.  Details about Shor's algorithm can be found in the following resource:

S. Beauregard, Circuit for shor’s algorithm using 2n+ 3 qubits, arXiv preprint quant-ph/0205095 (2002).

---

Import the following libraries:

	import matplotlib.pyplot as plt
	import numpy as np
	from qiskit import *
	from qiskit.visualization import plot_histogram
	from numpy.random import randint
	import pandas as pd
	from fractions import Fraction

- Begin by defining two variables, the number of counting qubits and some guess number a. For this code, N=15. Consider that for period r, a^(r)modN=1
and a<N. To start let's choose a=7.

- Now let's define a few key functions for Shor's algorithm. We'll start with a modular exponentiation function, which is used to map factorization problems
into period finding problems. Write a function that takes our guess number and some power as parameters. Generate a 4-qubit quantum circuit. For the sake of
not making this too easy, do not allow a to be a multiple of 3 or 5 and the
number 14, also 1 isn't very helpful so exclude that as well. Then use a a
for-loop to iterate over the range of the power parameter and then use a SWAP
gate to swap q0 & q1, q1 & q2, and q2 & q3. Note: the order of the SWAP gates matter. Then, still in the for loop, apply an X gate to each qubit. Convert the circuit into a gate and return the control version of that gate. This is hard-coded for a guess of 13, what if our guess was 2? What if it was 8? What if it
was 11? How would the code change?

- Next, let's define a quantum Fourier transform, which will elucidate the periodicity of the function. Start with an n-qubit quantum circuit. Iterate
over the first half of the qubits perform a swap gate between each qubit and
the corresponding qubit counting from the bottom (i.e. for a 4 qubit circuit,
q0 & q3 form a pair and q1 & q2 form a pair). Then create a for loop iterating over the qubits using an index (i). In the for loop create another for loop
that iterates over the index with a dummy index (k) and applies a controlled
phase (CP) gate with the arguments angle π/2^(i−k), control qubit k, and target qubit i. Then, in the outer for loop apply Hadamards to all "i" qubits. Return
the circuit.

- Now, let's apply the functions we created. Start by making a circuit that has 4 more qubits than the counting qubits , and a number of classical bits equal to
the number of counting qubits. The four additional qubits are for the modular exponentiation function to act on.

- Next, apply Hadamard gates to each counting qubit in the circuit. Then apply an
X gate on the last (auxiliary) qubits.

- Append the circuit to add the control modular exponentiation and quantum Fourier transform gates. Then measure the counting qubits.

- Simulate the circuit and generate a histogram of the counts.  Translate the binary numbers into their integer forms. Do they make sense?
