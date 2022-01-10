Consider a number between zero and $2^{n}-1$.  Then consider a function that can take that number as an input that will either always return a constant regardless of the input or will return one value for half the inputs and another for the remaining inputs.  Without access to the function itself, how do you know whether it is a constant function or a balanced function?  This is called Deutsch's problem.

One of the first quantum algorithms shown to outperform an analogous classical algorithm is the Deutsch-Jozsa algorithm.  This algorithm simply informs us if the function described in Deutsch's problem is constant or balanced.  In this module you will be guided on coding the Deutsch-Jozsa algorithm using Qiskit.

M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, USA, 2011) pp. 34–36.
