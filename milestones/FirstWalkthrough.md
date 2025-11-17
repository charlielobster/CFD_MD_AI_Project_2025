In this milestone, let's implement the <a href=https://docs.nvidia.com/physicsnemo/latest/user-guide/simple_training_example.html>Training Recipe</a> tutorial. 

It is based on this <a href=../papers/2010.08895v3.pdf>paper</a> about Fourier Neural Operators (FNO)s.

The paper's innovation is apparently the FNO. 

In addition to Darcy Flow, the paper also benchmarks against Burgers and Navier-Stokes Equations. 

The paper outlines the key differences between conventional solvers like FEM, FDM, LBM and similar solvers that do so by discretizing space. There is a trade-off in that step that forces a resolution on the results, and the paper points for the need for a continuous algorithm to do that. Data-driven Machine Learning and classical neural networks traditionally exist in finite-dimensional spaces, so although they are very good solvers for the resolution of the training data, apparently they are not very good at solving at other resolutions. 

The paper drills down into two existing PDE ML solvers, Finite-dimensional Operators and Neural-FEM, the former are by definition mesh-dependent and the later, although mesh-independent and accurate, suffers from issues due to the classical nature of its model. 


