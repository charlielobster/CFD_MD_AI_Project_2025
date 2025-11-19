# CFD and MD AI Modeling with the PhysicsNeMo Platform

<a href=https://developer.nvidia.com/physicsnemo>NVIDIA PhysicsNeMo Official Site</a>

This project is a general survey of and an experimental test-bed for the PhysicsNeMo API. According to the documentation, their Docker image is the preferred way to use the PhysicsNemo API for most cases. Original host is a manual CUDA Driver Ubuntu 24.04 installation described <a href=https://github.com/charlielobster/CUDA_NekRS.git>here</a>.

Some of these examples are about how to use Fourier Neural Operators (FNOs) and related AI operators to solve second order PDEs. Use these FNOs to augment results from standard CFD and MD algorithms, those traditional discrete PDE solvers for Navier-Stokes, etc. The output of a FNO-based AI model is continuous and mesh-invariant, and therefore scalable to arbitrary resolution and times.

To code along with this repository, fork NVIDIA's <a href=https://github.com/nvidia/physicsnemo.git>PhysicsNeMo</a>, or review my <a href=https://github.com/charlielobster/physicsnemo.git>fork</a> for any saved artifacts, results, or modifications. I've also <a href=https://github.com/charlielobster/PhysicsNeMo-Sym.git>forked </a> NVIDIA's <a href=https://github.com/nvidia/PhysicsNeMo-Sym>PhysicsNeMo-Sym</a> similarly.

## Project Milestones

<a href=milestones/RunDockerImage.md>Run PhysicsNemo Docker Container</a><br/>
<a href=milestones/FirstWalkthrough.md>First Walkthrough - Training Recipe</a><br/>

## Drill-Downs

<a href=drilldowns/Docker.md>Docker Drill-Down</a><br/>
<a href=drilldowns/Darcy.md>2D Darcy Flows</a><br/>
<a href=drilldowns/LBM.md>Lattice Boltzmann Solvers</a><br/>


## Related Papers and Summaries

<a href=papers/2010.08895v3.pdf>The Fourier Neural Operator for Parametric Partial Differential Equations</a> by Li et al. 2021<br/>
<a href=summaries/FNOs.md>FNO Summary</a><br/>
