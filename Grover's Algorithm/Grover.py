#A list of numbers to be searched for the number 8
secret_list=[4,3,5,6,7,8,1,2,9,3,0]

#defining the oracle with target of 8
def c_oracle(entry):
    target = 8
    if entry is target:
        answer = True
    else:
        answer = False
    return answer

#number of times the oracle is called and at what index in the list is the target
for index, test in enumerate(secret_list):
    if c_oracle(test) is True:
        print('The target was located at index %i.' %index)
        print('%i calls to the Oracle were used to find the target.' %(index+1))#recall that indices in Python start at 0
        break

from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as mpl
import numpy as np

#defining the oracle as a quantum circuit
q_oracle = QuantumCircuit(2,name='q_oracle')
q_oracle.cz(0,1) #flips the sign
q_oracle.to_gate()
q_oracle.draw(output='mpl')

grover = QuantumCircuit(2,2)
grover.h([0,1])#generating a superposition
grover.append(q_oracle,[0,1])
grover.draw(output='mpl')

backend = Aer.get_backend('statevector_simulator')#simulation
job = execute(grover,backend)
result=job.result()
state_vec=result.get_statevector()
print(state_vec)
#qubit-0 is in the |+> state and qubit-1 is in the |-> state
