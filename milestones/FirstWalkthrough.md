In this milestone, let's implement the <a href=https://docs.nvidia.com/physicsnemo/latest/user-guide/simple_training_example.html>Training Recipe</a> tutorial. 

It is based on this paper:<br/>
<a href=../papers/2010.08895v3.pdf>The Fourier Neural Operator for Parametric Partial Differential Equations</a> 
A conference paper at ICLR 2021 by Li, Kovachki, Azizzadenesheli, et al. 

The paper's innovation is the Fourier Neural Operator (FNO). 

The paper points out conventional solvers like Finite Element, Finite Difference, Lattice Boltzmann, Spectral, and similar solvers do so by discretizing space. In that step, there is a trade-off that forces a resolution on the results. The paper points for the need for a continuous algorithm to do that instead. Data-driven Machine Learning and classical neural networks traditionally exist in finite-dimensional spaces, so although they are very good solvers at the resolution of the training data, apparently they are not very good at solving at other resolutions. The paper drills down into two existing PDE ML solvers, Finite-dimensional Operators and Neural-FEM, the former are by definition mesh-dependent and the later, although mesh-independent and accurate, suffer from limitations due to the classical nature of their approach. 

The paper goes on to describe Neural Operators as a promising new methodology that is meshless and infinite-dimensional, and reviews existing Fourier Transform usage in ML. Their innovation is to define their neural operator in the Fourier space. Then it talks about how great it (FNO) is. Then it gets pretty mathy with all the gory details. Basically this involves wedging the Fourier space stuff (a bunch of FFTs and convolutions) into the Neural Operator definition. Then more stuff about how great it is - parameterization of R, invariance to discretization, quasi-linear complexity. 

In addition to Darcy Flow, the paper also benchmarks against Burgers and Navier-Stokes Equations. 

