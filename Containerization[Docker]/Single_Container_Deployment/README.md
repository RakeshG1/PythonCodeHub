# Single Docker Container Deployment

## Basic Docker Image Execution

**Docker Installaed Info**

```sh
# Docker version
$ docker --version
# Docker version 27.3.1, build ce12230

# Docker-compose version
$ docker-compose --version
# docker-compose version 1.29.2, build unknown
```

**Docker Images and Space**

```sh
# Docker images
$ docker images

#REPOSITORY            TAG       IMAGE ID       CREATED      SIZE
#jenkins/jenkins       lts       82a2134e1742   4 days ago   468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   7 days ago   1.38GB

# Docker consumed volume info
$ docker system df

#TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
#Images          2         2         1.849GB   0B (0%)
#Containers      2         0         431.6MB   431.6MB (100%)
#Local Volumes   2         2         522.5MB   0B (0%)
#Build Cache     0         0         0B        0B
```

**Build the Docker Image**

- Navigate to the directory containing the Dockerfile, requirements.txt, and app.py.

The command docker build -t simple-python-image . means:

- **`docker build`**: Build a Docker image from a Dockerfile.
- **`-t simple-python-image:latest`**: Tag the image with the name simple-python-image and latest is the tag for the image, which is commonly used to indicate the most recent version.
- **`.`**: The current directory (which contains the Dockerfile) is the build context, i.e., the location where Docker looks for the Dockerfile and any necessary files.

So, it builds an image named simple-python-image using the Dockerfile in the current directory.

```sh
# Build docker image
$ docker build -t simple-python-image:latest .

#[+] Building 48.8s (10/10) FINISHED                                                                                                                                                                  docker:default
# => [internal] load build definition from dockerfile                                                                                                                                                           0.1s
# => => transferring dockerfile: 460B                                                                                                                                                                           0.0s
# => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                            2.3s
# => [internal] load .dockerignore                                                                                                                                                                              0.0s
# => => transferring context: 2B                                                                                                                                                                                0.0s
# => [1/5] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda                                                                                     17.1s
# => => resolve docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda                                                                                      0.0s
# => => sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda 9.13kB / 9.13kB                                                                                                                 0.0s
# => => sha256:a66bd09b8d35bb52cd106a94c23a94ba22e6fde6bd13d6c5912ec4f5888a7f14 1.75kB / 1.75kB                                                                                                                 0.0s
# => => sha256:2c2c44fb54acb184dbedee948d7ba6460b1075a60a014d66857ce46543d4d840 5.29kB / 5.29kB                                                                                                                 0.0s
# => => sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260 28.21MB / 28.21MB                                                                                                               6.5s
# => => sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53 3.51MB / 3.51MB                                                                                                                 5.7s
# => => sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335 16.20MB / 16.20MB                                                                                                               8.8s
# => => sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f 249B / 249B                                                                                                                     6.1s
# => => extracting sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260                                                                                                                      5.9s
# => => extracting sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53                                                                                                                      0.5s
# => => extracting sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335                                                                                                                      3.5s
# => => extracting sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f                                                                                                                      0.0s
# => [internal] load build context                                                                                                                                                                              0.1s
# => => transferring context: 471B                                                                                                                                                                              0.0s
# => [2/5] WORKDIR /app                                                                                                                                                                                         0.7s
# => [3/5] COPY requirements.txt .                                                                                                                                                                              0.1s
# => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                  27.0s
# => [5/5] COPY app.py .                                                                                                                                                                                        0.1s 
# => exporting to image                                                                                                                                                                                         1.3s 
# => => exporting layers                                                                                                                                                                                        1.3s 
# => => writing image sha256:a8fac23adf133a318c3efbbb4d3de6e766dd4c6ebb9892a8051a4c372a714482                                                                                                                   0.0s 
# => => naming to docker.io/library/simple-python-image:latest                                                                                                                                                  0.0s 
```
>Note: 
- Each line in the dockerfile is becomes a layer, so while building this dockerfile as image using base image. Initially FROM base image layer prepared, then all lines in this dockerfile becomes layers like above. Once all layers prepared then file dockerimage like:- .zip file is prepared.
- While building, pulling or pushing docker images happens layer by layer just like uploadin zip with internal each directory by directory.
- Sometime layer size i.e., the command syntax in Dockerfile make its big or small layer. 
    - Like syntax pip install deep-learning-libs in Dockerfile, makes this layer make it very big layer.   
    - Like WORKDIR /app simple command in Dockerfile, makes this layer make it small layer.
- Its all ways good way to maintain moderate layer size not so big, hence it becomes slow in download or upload to registry.
- Each layer will have unique hashmap key.

Docker Image Info

```sh
$ docker images

#REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
#simple-python-image   latest    a8fac23adf13   18 seconds ago   288MB
#jenkins/jenkins       lts       82a2134e1742   4 days ago       468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   7 days ago       1.38GB
```

Do some code changes in Dockerfile/app.py

```sh
# Create new docker image with latest changes
$ docker build -t simple-python-image:latest .

#[+] Building 29.3s (10/10) FINISHED                                                                                                                                                            docker:default
# => [internal] load build definition from dockerfile                                                                                                                                                     0.0s
# => => transferring dockerfile: 460B                                                                                                                                                                     0.0s
# => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                      1.1s
# => [internal] load .dockerignore                                                                                                                                                                        0.0s
# => => transferring context: 2B                                                                                                                                                                          0.0s
# => [1/5] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda                                                                                0.0s
# => [internal] load build context                                                                                                                                                                        0.0s
# => => transferring context: 338B                                                                                                                                                                        0.0s
# => CACHED [2/5] WORKDIR /app                                                                                                                                                                            0.0s
# => [3/5] COPY requirements.txt .                                                                                                                                                                        0.1s
# => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                            26.5s
# => [5/5] COPY app.py .                                                                                                                                                                                  0.1s 
# => exporting to image                                                                                                                                                                                   1.4s 
# => => exporting layers                                                                                                                                                                                  1.4s 
# => => writing image sha256:e4f5497177ebab415d993599902a25d8fbc0ac2e3faac02bc8e4a3c02643e554                                                                                                             0.0s 
# => => naming to docker.io/library/simple-python-image:latest
```

>Note: It only update the layer/syntax line in Dockerfile, which got new changes.

**Create & Run the Docker Container**

- Once the image is built, create & run the Docker container again:

```sh
$ docker run --name simple-pandas-container simple-python-image/a8fac23adf13

# Docker images info
$ docker images

#REPOSITORY            TAG       IMAGE ID       CREATED              SIZE
#simple-python-image   latest    e4f5497177eb   About a minute ago   288MB
#<none>                <none>    a8fac23adf13   14 minutes ago       288MB
#jenkins/jenkins       lts       82a2134e1742   4 days ago           468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   7 days ago           1.38GB

# Already docker container created we have to remove it along with its underlying volumne
$ docker run --name simple-pandas-container simple-python-image

#docker: Error response from daemon: Conflict. The container name "/simple-pandas-container" is already in use by container "abadb837d2ef26c0a79c7f96ca0e94e7287e2f194ab4c356b24e36caeadc1e7d". You have to remove (or #rename) that container to be able to reuse that name.
#See 'docker run --help'.

# Check docker container
$ docker ps -a

#CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS                     PORTS     NAMES
#abadb837d2ef   a8fac23adf13          "python app.py"          4 minutes ago   Exited (1) 4 minutes ago             simple-pandas-container
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago      Exited (143) 2 days ago              bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago      Exited (143) 2 days ago              jenkins

# Remove container and its volumne
$ docker rm -v abadb837d2ef
#abadb837d2ef

# Removing along with volume, we can see that taggling image(which is not been tied any container) will also be removed
$ docker images

#REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
#simple-python-image   latest    e4f5497177eb   14 minutes ago   288MB
#jenkins/jenkins       lts       82a2134e1742   4 days ago       468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   7 days ago       1.38GB

$ docker ps -a

#CONTAINER ID   IMAGE                 COMMAND                  CREATED      STATUS                    PORTS     NAMES
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago   Exited (143) 2 days ago             bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago   Exited (143) 2 days ago             jenkins

# Now create docker container again with latest docker image
$ docker run --name simple-pandas-container simple-python-image
     
#     name  cost
#0   apple    10
#1  banana     5
#2  orange     6

$ docker ps -a

#CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS                      PORTS     NAMES
#2f0e894aa41c   simple-python-image   "python app.py"          13 minutes ago   Exited (0) 13 minutes ago             simple-pandas-container
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago       Exited (143) 2 days ago               bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago       Exited (143) 2 days ago               jenkins
```

**Run the Docker Container (which is stoppped)**

Our python code just runs and exist. Not like continously running code. So 'Exited (0) 13 minutes ago' means executed successfully and exited.

```sh
$ docker start simple-pandas-container

# simple-pandas-container
```

> Note: docker run i.e., container create & run showing python output. But docker start i.e., container start (already created container) not showing python print output

**Stop the Docker Container (which is running)**

```sh
$ docker stop simple-pandas-container
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

## Different types of Python file execution

- **`CMD python app.py (in Dockerfile):`**
- This command is used in the Dockerfile to set the default command that runs when the container starts.
- It makes the container run python app.py automatically when you start the container without specifying any other command.
- Example in Dockerfile:

```sh
CMD ["python", "app.py"]
```

- Pro: Simpler and automatic execution of the Python script when the container starts.
- Con: You can't easily override the command when running the container.

- **`docker run --name my-python-container my-python-image python /path/to/your/app.py (command when running the container):`**
- This command specifies the command to run (python /path/to/your/app.py) when you start the container.

```sh
docker run --name python-pandas-container simple-python-image python /app/app.py
```

- It overrides any CMD set in the Dockerfile, allowing you to specify different commands at runtime.
- Pro: Flexibility to run different commands or scripts without modifying the Dockerfile.
- Con: You need to specify the command every time you run the container.

- **`In short:`**
- CMD python app.py: Runs automatically when the container starts, based on the Dockerfile.
- docker run ... python app.py: Lets you specify a command at runtime, overriding the Dockerfile's CMD.

## Mounting a file [External Volume]

- **`Mounting a Volume (-v)`**: Mounts a file or directory from your host machine into the container. The first part (/path/to/local/csv) is the local path, and the second part (/path/in/container/csv) is the container path where the file will be accessible.

- **`Running the Script`**: The Python script will use pandas to read the CSV file from the mounted path and process it into a DataFrame.

This setup ensures that the container can read the CSV file during runtime without the need to include the file inside the image.

```sh
# Docker images info
rga@rgavm:~$ docker images
#REPOSITORY            TAG       IMAGE ID       CREATED      SIZE
#jenkins/jenkins       lts       82a2134e1742   4 days ago   468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   8 days ago   1.38GB

# Docker container status
rga@rgavm:~$ docker ps -a
#CONTAINER ID   IMAGE                 COMMAND                  CREATED      STATUS                    PORTS     NAMES
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago   Exited (143) 2 days ago             bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago   Exited (143) 2 days ago             jenkins

# Docker volumes info
rga@rgavm:~$ docker system df
#TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
#Images          2         2         1.849GB   0B (0%)
#Containers      2         0         431.6MB   431.6MB (100%)
#Local Volumes   2         2         522.5MB   0B (0%)
#Build Cache     17        0         316.4MB   316.4MB

# Show content
rga@rgavm:~$ cat /home/rga/data/dummy.csv | head -n 5
#apple,banana,orange
#10,5,6rga@rgavm:~$ 

rga@rgavm:~$ cd /mnt/Local/Git_Repo/PythonCodeHub/Containerization\[Docker\]/Single_Container_Deployment/

# Show files list
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ ls -la
#total 34
#drwxrwxrwx 1 root root  4096 Feb  9 16:01 .
#drwxrwxrwx 1 root root  4096 Feb  9 18:43 ..
#-rwxrwxrwx 1 root root   252 Feb  9 15:09 app.py
#drwxrwxrwx 1 root root     0 Feb  9 16:01 data
#-rwxrwxrwx 1 root root   441 Feb  9 16:10 dockerfile
#-rwxrwxrwx 1 root root   250 Feb  9 16:12 ext_app.py
#-rwxrwxrwx 1 root root 24098 Feb  9 16:04 README.md
#-rwxrwxrwx 1 root root     6 Feb  9 15:09 requirements.txt

# Build docker image
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker build -t simple-python-image:latest .
#[+] Building 1.6s (11/11) FINISHED                                                                                                                                                                                                                                  docker:default
# => [internal] load build definition from dockerfile                                                                                                                                                                                                                          0.0s
# => => transferring dockerfile: 480B                                                                                                                                                                                                                                          0.0s
# => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                                                                                           1.4s
# => [internal] load .dockerignore                                                                                                                                                                                                                                             0.0s
# => => transferring context: 2B                                                                                                                                                                                                                                               0.0s
# => [1/6] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda                                                                                                                                                     0.0s
# => [internal] load build context                                                                                                                                                                                                                                             0.0s
# => => transferring context: 93B                                                                                                                                                                                                                                              0.0s
# => CACHED [2/6] WORKDIR /app                                                                                                                                                                                                                                                 0.0s
# => CACHED [3/6] COPY requirements.txt .                                                                                                                                                                                                                                      0.0s
# => CACHED [4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                                                                           0.0s
# => CACHED [5/6] COPY app.py .                                                                                                                                                                                                                                                0.0s
# => CACHED [6/6] COPY ext_app.py .                                                                                                                                                                                                                                            0.0s
# => exporting to image                                                                                                                                                                                                                                                        0.0s
# => => exporting layers                                                                                                                                                                                                                                                       0.0s
# => => writing image sha256:020ec9867f0f4eebcb68e99a1c31489754c3e14052c467f3348a846ef57fa363                                                                                                                                                                                  0.0s
# => => naming to docker.io/library/simple-python-image:latest                                                                                                                                                                                                                 0.0s

# Show docker images
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker images
#REPOSITORY            TAG       IMAGE ID       CREATED       SIZE
#simple-python-image   latest    020ec9867f0f   3 hours ago   288MB
#jenkins/jenkins       lts       82a2134e1742   4 days ago    468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   8 days ago    1.38GB

# Login container as shell session, so to view all files in this container
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker run --name python-pandas-ext-container -v /home/rga/data/dummy.csv:/app/dummy.csv -it simple-python-image bash

# Show file
root@c39b1eaf22cf:/app# cat /app/dummy.csv 
#apple,banana,orange
#10,5,6root@c39b1eaf22cf:/app# 

# Exit container
root@c39b1eaf22cf:/app# exit
#exit

# Alread docker container exists with this name, so it should be removed
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker run --name python-pandas-ext-container -v /home/rga/data/dummy.csv:/app/dummy.csv simple-python-image python /app/ext_app.py
#docker: Error response from daemon: Conflict. The container name "/python-pandas-ext-container" is already in use by container "c39b1eaf22cfcf45da4f5e8501c12ea3f6fdc1a2fc28236770c214c61f260153". You have to remove (or rename) that container to be able to reuse that name.
#See 'docker run --help'.

# Check docker container status
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker ps -a
#CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS                            PORTS     NAMES
#c39b1eaf22cf   simple-python-image   "bash"                   About a minute ago   Exited (130) About a minute ago             python-pandas-ext-container
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago           Exited (143) 2 days ago                     bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago           Exited (143) 2 days ago                     jenkins

# Remove container along with its volume
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker rm -v c39b1eaf22cf
#c39b1eaf22cf

# Create docker container with mounted volume file and execute docker container
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker run --name python-pandas-ext-container -v /home/rga/data/dummy.csv:/app/dummy.csv simple-python-image python /app/ext_app.py
#   apple  banana  orange
#0     10       5       6

# Check docker container status
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Single_Container_Deployment$ docker ps -a
#CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS                     PORTS     NAMES
#063f85c8ba19   simple-python-image   "python /app/ext_app…"   10 seconds ago   Exited (0) 6 seconds ago             python-pandas-ext-container
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago       Exited (143) 2 days ago              bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 days ago       Exited (143) 2 days ago              jenkins
```