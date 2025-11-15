This project requires the Nvidia PhysicsNeMo API. 
It may also require a docker installation, as this is the suggested way to use the PhysicsNemo API, according to their documentation.

For an Ubuntu 24.04 installation, 

Install Docker

Official Install Docs here: https://docs.docker.com/desktop/setup/install/linux/

On Ubuntu, Docker requires `kvm`

```
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```

I had to reboot before the connection to QEMU/KVM would take

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

From the above link, install docker via `apt`:

```
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
```

Then install docker

```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

<img src="images/docker_status.png" />


Check with a call to hello world:

<img src="images/docker_hello_world.png" />

Then install Nvidia Container Toolkit
