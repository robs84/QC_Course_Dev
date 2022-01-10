import matplotlib.pyplot as plt
import numpy as np
from qiskit import *
from qiskit.visualization import plot_histogram
from numpy.random import randint
import pandas as pd
from fractions import Fraction

#variables
counting = 8
a = 7

def amod15(a, power):
    Mod = QuantumCircuit(4)
    for j in range(power):
        Mod.swap(2,3)
        Mod.swap(1,2)
        Mod.swap(0,1)
        for qubit in range(4):
            Mod.x(qubit)
    Mod = Mod.to_gate()
    Mod.name = "%i^%i mod 15" % (a, power)
    c_Mod = Mod.control()
    return c_Mod

def qft(n):
    qft = QuantumCircuit(n)
    for qubit in range(n//2):
        qft.swap(qubit, n-qubit-1)
    for i in range(n):
        for k in range(i):
            qft.cp(-np.pi/float(2**(i-k)), k, i)
        qft.h(i)
    qft.name = "QFT"
    return qft

shor = QuantumCircuit(counting + 4, counting)
#initialize counting qubits into the |+> state
for q in range(counting):
    shor.h(q)
# auxiliary register in state |1>
shor.x(3+counting)
shor.draw(output='mpl')
# controlled-gate operations
for q in range(counting):
    shor.append(amod15(a, 2**q), [q]+[i+counting for i in range(4)])
shor.append(qft(counting), range(counting))
shor.measure(range(counting), range(counting))
shor.draw(output='mpl')

backend = Aer.get_backend('qasm_simulator')
results = execute(shor, backend, shots = 1000).result()
counts = results.get_counts()
plot_histogram(counts)
