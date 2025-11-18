In this milestone, let's implement the <a href=https://docs.nvidia.com/physicsnemo/latest/user-guide/simple_training_example.html>Training Recipe</a> tutorial. 

It is based on this paper:<br/>
<a href=../papers/2010.08895v3.pdf>The Fourier Neural Operator for Parametric Partial Differential Equations</a><br/>
A conference paper at ICLR 2021 by Li, Kovachki, Azizzadenesheli, et al. 

The paper's innovation is the Fourier Neural Operator (FNO). 

The paper points out conventional solvers like Finite Element, Finite Difference, Lattice Boltzmann, Spectral, and similar solvers do so by discretizing space. In that step, there is a trade-off that forces a resolution on the results. The paper points for the need for a continuous algorithm to do that instead. 

Data-driven Machine Learning and classical neural networks traditionally exist in finite-dimensional spaces, so although they are very good solvers at the resolution of the training data, they are not very good at solving for other resolutions. The paper drills down into two existing PDE ML solvers, Finite-dimensional Operators and Neural-FEM. The former are by definition mesh-dependent, and the later, although mesh-independent and accurate, suffer from limitations due to the classical nature of their approach. 

The paper goes on to describe Neural Operators as a promising new methodology that is meshless and infinite-dimensional, and reviews existing Fourier Transform usage in ML. The paper's innovation is to define their neural operator's kernel integral operator in Fourier space. It gets pretty mathy with all the gory details. Basically this involves wedging the Fourier space stuff (a bunch of FFTs and convolutions) into the Neural Operator definitions (a bunch of definitions including kernel integral operators, updates, and activation functions). It reviews FNO's three key features: parameterization of R, invariance to discretization, and quasi-linear complexity. 

In addition to Darcy Flow, the paper also benchmarks against the Burgers and Navier-Stokes Equations, all of which it spends some time defining. It benchmarks FNO results to other neural network architectures. It concludes with a section on two interesting features, that FNO is capable of zero-shot super-resolution, and of solving the Bayesian Inverse Problem.

