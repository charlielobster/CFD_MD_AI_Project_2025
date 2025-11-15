This project requires the Nvidia PhysicsNeMo API. 
It may also require a docker installation, as this is the suggested way to use the PhysicsNemo API, according to their documentation.

For an Ubuntu 24.04 installation, 

Install Docker

Official Install Docs here: https://docs.docker.com/desktop/setup/install/linux/

On Ubuntu, Docker requires kvm

```
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```

I had to reboot before the usermod settings would take

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository





AI Suggestions for Docker:

Update packages and certificates
```
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```
Add Docker's official GPG key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

