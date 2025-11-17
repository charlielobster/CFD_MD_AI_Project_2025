# Docker Drill-Down

This drill-down assumes completion of this <a href=../milestones/RunDockerImage.md>milestone</a>. 

Docker is used for running a virtual machine (vm) inside a host. In Docker, the vm is created from an `image`, which acts like a recipe. Once instantiated, the vm instance is referred to as a `container`. Unless a shared folder is specified, any changes done locally within in the container will be lost, unless the container is first saved back into an image. An important best practice is therefore to keep data in a shared folder passed to the container.

## Basic Operations

### Run (Latest PhysicsNeMo) Image

Let's break down this call to `docker run`:

```
sudo docker run \
    --gpus all \
    --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    --runtime nvidia \
    --rm \
    -it \
    -v host_folder:container_folder \
    nvcr.io/nvidia/physicsnemo/physicsnemo:25.06 \
    bash
```
`--shm-size=1g` Allocate 1 gig to `/dev/shm`<br/>
`--runtime nvidia` Use the NVIDIA Container runtime<br/>
`--rm` Automatically remove this container and its associated anonymous volumes when exiting<br/>
`-it` Interactive, allocate a pseudo-TTY<br/>
`-v host_folder:container_folder` Share folder between container and image<br/>
`nvcr.io/nvidia/physicsnemo/physicsnemo:25.06` Selected image to run<br/>
`bash` Selected terminal shell language<br/>

### Save Container Into Image

Get Docker Container ID

```
sudo docker ps
```

Save Changes to Docker Image

```
sudo docker commit <container_id> image:version
```
