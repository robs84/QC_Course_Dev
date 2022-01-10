# Entanglement
************

Introduction to superposition and entanglement will highlight two frequently used gates, the Hadamard and CNOT (or CX) gates.  The Hadamard gate takes a qubit of known state and yields a normalized linear combination of states in that basis.  The CNOT gate will perform a NOT operation on the second qubit if the first (control) qubit is $|1\rangle$ and will not perform any operation if the control qubit is $|0\rangle$, in the computational basis.

---

In this module we will look at both superposition and entanglement using the Hadamard and CNOT gates. The learning objective is to gain an intuition about these fundamental operations.

- Begin by generating a quantum circuit composed of a 2-qubit quantum register
and a 2-bit classical register.

- To the first qubit apply a Hadamard gate and then apply a controlled X gate
between the two qubits.  Measure both qubits and comment on the results.

- Now, repeat the process with a second Hadamard on the first qubit before the CNOT and again after the CNOT. Comment on what happens in both scenarios. This logic can be worked out somewhat trivially using Dirac notation.
