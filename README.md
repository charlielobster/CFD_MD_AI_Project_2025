# CFD and MD AI Modeling with PhysicsNeMo API

<a href=https://developer.nvidia.com/physicsnemo>NVIDIA PhysicsNeMo Official Site</a>

This project is a general survey of and an experimental test-bed for the PhysicsNeMo API. According to the documentation, their Docker image is the preferred way to use the PhysicsNemo API for most cases. Original host is a manual CUDA Driver Ubuntu 24.04 installation described <a href=https://github.com/charlielobster/CUDA_NekRS.git>here</a>.

This mainly seems to be about how to use Fourier Neural Operators (FNOs) and related AI models to solve Second Order PDEs. Then it is about how to use these FNOs to augment results from standard CFD and MD algorithms, those traditional solvers for Navier-Stokes, Lattice Boltzmann, etc. The output of a FNO-based AI model is continuous and mesh-invariant, and therefore scalable to arbitrary resolution and times.

## Project Milestones

<a href=milestones/RunDockerImage.md>Run PhysicsNemo Docker Container</a><br/>
<a href=milestones/FirstWalkthrough.md>First Walkthrough - Training Recipe</a><br/>

## Drill-Downs

<a href=drilldowns/Docker.md>Docker Drill-Down</a><br/>
<a href=drilldowns/Darcy.md>2D Darcy Flows</a><br/>
<a href=drilldowns/LBM.md>Lattice Boltzmann Solvers</a><br/>
<a href=drilldowns/NoDocker.md>Direct Installation? True Tales of Pros and Cons</a>
