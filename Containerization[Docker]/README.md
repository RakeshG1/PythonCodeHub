### Setup Docker[Ubuntu]

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

- ``View Docker Containers Status``
```bash
$ docker ps
# CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

- ``View Existing Docker Images``
```bash
$ docker images
# REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

- ``Run Docker Container``
```bash
$ docker run hello-world
$ docker images
#REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
#hello-world   latest    d2c94e258dcb   18 months ago   13.3kB
```