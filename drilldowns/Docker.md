# Docker Drill-Down

## Some Docker Details

This drill-down assumes completion of this <a href=../milestones/RunDockerImage.md>milestone</a>. 

Docker is used for running a virtual machine (vm) inside a host. In Docker, the virtual machine is created from an `image`, which acts like a recipe for the vm. Once instantiated, the vm instance is referred to as a `container`. Unless a shared folder is specified, any changes done locally within in the container will be lost, unless the container is first saved back into an image. Therefore, an important best practice is to keep data in a shared folder passed to the container.

## Basic Operations

### Run Latest PhysicsNeMo Image

```
sudo docker run \
    --gpus all \
    --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    --runtime nvidia \
    --rm \
    -it \
    nvcr.io/nvidia/physicsnemo/physicsnemo:25.06 \
    bash
```
Let's break this down, 

`--rm` Automatically remove this container and its associated anonymous volumes when exiting<br/>
`-it` Interactive, allocate a pseudo-TTY<br/>
`--shm-size=1g` Allocate 1 gig to `/dev/shm`<br/>
`--runtime nvidia` Use the NVIDIA Container Toolkit runtime

### Save Container Into Image

Get Docker Container ID

```
sudo docker ps
```

Save Changes to Docker Image

```
sudo docker commit <container_id> image:version
```

### Share Folder Between Container and Image

We need to add `-v` to the docker run call.

```
-v /home/user/my_data:/app/data my_app_image
```
Here, `/home/user/my_data` is the folder name on the host, and `/app/data` will be the folder name in the container.
