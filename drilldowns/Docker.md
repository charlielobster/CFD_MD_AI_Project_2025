# Docker Drill-Down

## Understanding Docker

Docker is used for running a virtual machine on top of an existing host. Unless a shared folder is specified, any changes done within the contents of the container will be lost unless the container is saved as an image. This Drill-Down assumes completion of this <a href=../milestones/RunDockerImage.md>milestone</a>.

## Basic Operations

### Run Latest PhysicsNeMo Image

```
sudo docker run --gpus all --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 --runtime nvidia --rm -it nvcr.io/nvidia/physicsnemo/physicsnemo:25.06 bash
```

### Share Folder Between Container and Image
