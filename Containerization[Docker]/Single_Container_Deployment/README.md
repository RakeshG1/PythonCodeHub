### Single Docker Container Deployment

**Build the Docker Image**

- Navigate to the directory containing the Dockerfile, requirements.txt, and app.py.

```sh
$ docker build -t python-pandas-image .
```

**Create & Run the Docker Container**

- Once the image is built, run the Docker container:

```sh
$ docker run --name python-pandas-container python-pandas-image

#     name  cost
# 0   apple    10
# 1  banana     5
# 2  orange     6
```

**Check Docker Container**

```sh
# Docker version
$ docker --version
#Docker version 27.3.1, build ce12230

# Docker-compose version
$ docker-compose --version
#docker-compose version 1.29.2, build unknown

# Docker images
$ docker images
# REPOSITORY            TAG       IMAGE ID       CREATED         SIZE
# python-pandas-image   latest    64afb18b2a8c   2 minutes ago   273MB
# hello-world           latest    d2c94e258dcb   19 months ago   13.3kB

# Docker container's details both (running and stopped)
$ docker ps -a
CONTAINER ID   IMAGE                 COMMAND           CREATED       STATUS                   PORTS     NAMES
58323972c3e7   python-pandas-image   "python app.py"   4 hours ago   Exited (0) 4 hours ago             python-pandas-container
fd85d616dabc   hello-world           "/hello"          7 days ago    Exited (0) 7 days ago              tender_greider
```

**Run the Docker Container (which is stoppped)**

```sh
$ docker start python-pandas-container
```

**Stop the Docker Container (which is running)**

```sh
$ docker stop python-pandas-container
```

**View Docker Container Logs (which is running/stopped)**

```sh
$ docker logs python-pandas-container
#     name  cost
#0   apple    10
#1  banana     5
#2  orange     6

$ docker logs --tail 4 -f python-pandas-container
#     name  cost
#0   apple    10
#1  banana     5
#2  orange     6
```