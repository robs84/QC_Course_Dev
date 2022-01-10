In this module you will look at rotations about the Bloch sphere using fundamental one-qubit operations such as the Pauli gates, the Hadamard gate, and the rotational gates S and T. The learning objective is to explore Bloch sphere rotations, visualization, and develop an intuition about what these fundamental operations do to the qubit.

Begin by creating a one-qubit register (do not forget to include a classical register for measurement).
By default, Qiskit will initialize your qubit in the |0> state. Then visualize the Bloch sphere and print the state vector for your qubit state.

Now, apply a Pauli X gate (also known as a NOT gate) and repeat the process to observe how the state vector changes.

Let's simulate this in a quantum computer to validate the fidelity of the operation.

Repeat the above visualization process for the Pauli Y and Z gates to see what each gate does to the |0> state. What do you observe? Explain why the changes, if any, occurred?

Now, rebuild the circuit to view the action of the Hadamard gate on our qubit and visualize using the Bloch sphere.

Okay, so we have seen rotations from the |0> state to the |1> state and the |+> state (+x-direction).

Now, using the Pauli, Hadamard, and S gates rotate the along the Bloch sphere to align the state vector with |-> (-x-direction), |R> (+y-direction), and |L> (-y-direction).

For completeness, create a circuit composed of the Hadamard and T gates and visualize on the Bloch sphere.

Now repeat the entire process, but initialize the qubit to be in the |1> state. What changes and why?
