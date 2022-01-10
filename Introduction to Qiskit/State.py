from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import plot_bloch_multivector

#building a 1-qubit circuit
circ1 = QuantumCircuit(1,1)

#uncomment below to start in the |1> state
#circ1.initialize([0,1], 0)

#simulating the state vector
sim = Aer.get_backend('statevector_simulator')
result_sv1 = execute(circ1, backend = sim).result()
state_vec1 = result_sv1.get_statevector()
#printing the state vector and visualizing it on the Bloch sphere
print(state_vec1)
plot_bloch_multivector(state_vec1)

#adding an X gate
circ1.x(0)
circ1.draw(output = 'mpl')

sim = Aer.get_backend('statevector_simulator')
result_sv1 = execute(circ1, backend = sim).result()
state_vec1 = result_sv1.get_statevector()
print(state_vec1)
plot_bloch_multivector(state_vec1)

circ1.measure([0],[0])
simulator = Aer.get_backend('qasm_simulator')
result_c1 = execute(circ1, backend = simulator, shots = 1000).result()
count1 = result_c1.get_counts()
plot_histogram(count1)

circ2 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ2.initialize([0,1], 0)
circ2.y(0)
circ2.draw(output = 'mpl')

result_sv2 = execute(circ2, backend = sim).result()
state_vec2 = result_sv2.get_statevector()
print(state_vec2)
plot_bloch_multivector(state_vec2)

circ3 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ3.initialize([0,1], 0)
circ3.z(0)
circ3.draw(output = 'mpl')

result_sv3 = execute(circ3, backend = sim).result()
state_vec3 = result_sv3.get_statevector()
print(state_vec3)
plot_bloch_multivector(state_vec3)

circ4 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ4.initialize([0,1], 0)
circ4.h(0)
circ4.draw(output = 'mpl')

result_sv4 = execute(circ4, backend = sim).result()
state_vec4 = result_sv4.get_statevector()
print(state_vec4)
plot_bloch_multivector(state_vec4)

circ5 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ5.initialize([0,1], 0)
circ5.x(0)
circ5.h(0)
circ5.draw(output = 'mpl')

result_sv5 = execute(circ5, backend = sim).result()
state_vec5 = result_sv5.get_statevector()
print(state_vec5)
plot_bloch_multivector(state_vec5)

circ6 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ6.initialize([0,1], 0)
circ6.h(0)
circ6.s(0)
circ6.draw(output = 'mpl')

result_sv6 = execute(circ6, backend = sim).result()
state_vec6 = result_sv6.get_statevector()
print(state_vec6)
plot_bloch_multivector(state_vec6)

circ7 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ7.initialize([0,1], 0)
circ7.h(0)
circ7.s(0)
circ7.z(0)
circ7.draw(output = 'mpl')

result_sv7 = execute(circ7, backend = sim).result()
state_vec7 = result_sv7.get_statevector()
print(state_vec7)
plot_bloch_multivector(state_vec7)

circ8 = QuantumCircuit(1,1)
#uncomment below to start in the |1> state
#circ8.initialize([0,1], 0)
circ8.h(0)
circ8.t(0)
circ8.draw(output = 'mpl')

result_sv8 = execute(circ8, backend = sim).result()
state_vec8 = result_sv8.get_statevector()
print(state_vec8)
plot_bloch_multivector(state_vec8)
