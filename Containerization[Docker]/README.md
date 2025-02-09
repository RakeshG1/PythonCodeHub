## Setup Docker[Ubuntu]

- ``Install Docker & Docker-Compose``
```bash
$ sudo apt-get update

$ sudo apt-get install ca-certificates curl

$ sudo install -m 0755 -d /etc/apt/keyrings

$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

$ sudo chmod a+r /etc/apt/keyrings/docker.asc

$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

$ sudo apt install docker-compose
```

- ``Adding Docker to sudo group[execute without sudo user]``
```bash
$ sudo usermod -aG docker $USER
$ newgrp docker
```

- ``View Docker & Docker-Compose Versions``
```bash
$ docker --version
# Docker version 27.3.1, build ce12230
$ docker-compose --version
# docker-compose version 1.29.2, build unknown
```

- ``View files size in container``

```sh
docker exec -it <container_name_or_id> du -sh /*  # Shows the disk usage for each top-level directory
docker exec -it <container_name_or_id> du -sh /usr/src/app/*  # Shows the disk usage for files under /usr/src/app
```

## Difference between different Base Python Images

- **`Slim`**: Use when you need a small image and are okay with managing dependencies yourself.
- **`Alpine`**: Use for an ultra-lightweight image, but be prepared for extra setup work.
- **`Buster`**: Use when you want a more stable image with a wider range of pre-installed tools and dependencies.
- **`Ubuntu`**: Use for maximum compatibility and ease of use, especially when working with more complex setups.

and the Images are ex:- FROM python:3.11-slim

- **`python:3.11`**: This is the default Python 3.11 image, which is Debian-based (Buster) and includes necessary libraries to run Python, but it may have more overhead than slim or alpine.
- **`python:3.11-slim`**: A minimal image based on Debian, with unnecessary files removed, resulting in a smaller image size. Use this for smaller container sizes but may require manual installation of some dependencies.
- **`python:3.11-alpine`**: The most lightweight image, based on Alpine Linux. It’s much smaller but might need extra setup to install some dependencies due to its minimalism.
- **`python:3.11-buster`**: The Debian Buster-based version, providing a stable environment with a larger size compared to the slim version, but with more out-of-the-box compatibility for certain packages.
- **`python:3.11-ubuntu`**: A version based on Ubuntu, which is larger but more compatible with certain libraries and tools compared to Alpine or Slim.