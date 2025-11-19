# CFD and MD AI Modeling with PhysicsNeMo API

<a href=https://developer.nvidia.com/physicsnemo>NVIDIA PhysicsNeMo Official Site</a>

This project is a general survey of and an experimental test-bed for the PhysicsNeMo API. According to the documentation, their Docker image is the preferred way to use the PhysicsNemo API for most cases. Original host is a manual CUDA Driver Ubuntu 24.04 installation described <a href=https://github.com/charlielobster/CUDA_NekRS.git>here</a>.

Much of these examples may be how to use Fourier Neural Operators (FNOs) and related AI operators to solve Second Order PDEs. Use these FNOs to augment results from standard CFD and MD algorithms, those traditional discrete PDE solvers for Navier-Stokes, etc. The output of a FNO-based AI model is continuous and mesh-invariant, and therefore scalable to arbitrary resolution and times.

Fork the PhysicsNeMo examples <a href=https://github.com/nvidia/physicsnemo.git>repository</a>, or review my <a href=https://github.com/charlielobster/physicsnemo.git>fork</a> for any saved artifacts, results, or modifications. I've also forked <a href=https://github.com/charlielobster/PhysicsNeMo-Sym.git>PhysicsNeMo-Sym</a> similarly.

## Project Milestones

<a href=milestones/RunDockerImage.md>Run PhysicsNemo Docker Container</a><br/>
<a href=milestones/FirstWalkthrough.md>First Walkthrough - Training Recipe</a><br/>

## Drill-Downs

<a href=drilldowns/Docker.md>Docker Drill-Down</a><br/>
<a href=drilldowns/FNOs.md>Fourier Neural Operators</a><br/>
<a href=drilldowns/Darcy.md>2D Darcy Flows</a><br/>
<a href=drilldowns/LBM.md>Lattice Boltzmann Solvers</a><br/>

