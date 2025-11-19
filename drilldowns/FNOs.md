A Brief Summary of <a href=../papers/2010.08895v3.pdf>The Fourier Neural Operator for Parametric Partial Differential Equations</a><br/>
A conference paper at ICLR 2021 by Li, Kovachki, Azizzadenesheli, et al. 

The paper's innovation is the Fourier Neural Operator (FNO). 

The paper points out conventional solvers like Finite Element, Finite Difference, Lattice Boltzmann, Spectral Element, and similar solvers do so by discretizing space. In that step, there is a trade-off that forces a resolution on the results. In a similar vein, each step t in time must be computed first in order to determine the results at some t + 1 time. The paper points to the need for a continuous algorithm to do all that instead. 

Data-driven Machine Learning (ML) and classical neural networks traditionally exist in finite-dimensional spaces, so although they are very good solvers at the resolution of the training data, they are not very good at solving for other resolutions. The paper drills down into two existing PDE ML solvers, Finite-dimensional Operators and Neural-FEM. The former are by definition mesh-dependent, and the latter, although mesh-independent and accurate, suffer from limitations due to the classical nature of their approach. 

The paper goes on to describe Neural Operators as a promising new methodology that is meshless and infinite-dimensional, and then briefly reviews existing Fourier Transform usage in ML. The paper's innovation is then to define their version of the neural operator's kernel integral operator in Fourier space. It gets pretty mathy with all the gory details. Basically this involves wedging the Fourier space stuff (a bunch of FFTs and convolutions) into the Neural Operator definitions (a bunch of set theory-ish definitions including kernel integral operators, updates, and activation functions). It reviews FNO's three key features: parameterization of R, invariance to discretization, and quasi-linear complexity. 

In addition to benchmarking with 2D Darcy Flow, the paper also benchmarks with the Burgers and Navier-Stokes Equations. It takes some time defining each of these formally. It benchmarks FNO results against other neural network architectures. The paper concludes with a section on two interesting features; FNO is capable of zero-shot super-resolution, and it can solve the Bayesian Inverse Problem.

