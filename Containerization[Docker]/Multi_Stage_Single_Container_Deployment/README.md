# Single vs. Multi-stage Dockerfile

## Single-stage Dockerfile:

- Involves a single image used to build and run the application.
- All dependencies, including build tools, remain in the final image, which can result in a larger image size.

## Multi-stage Dockerfile:

- Uses multiple FROM statements to create different stages.
- The final image only includes the necessary artifacts for running the application, such as the application code and required runtime dependencies.
- Reduces image size by separating build dependencies from runtime dependencies.

## Benefits of Multi-stage Builds:

- **`Smaller Final Image`**: Only the required runtime components are included, reducing image size.
- **`Cleaner and More Efficient`**: Build tools and dependencies are discarded after the build phase.
- **`Improved Security`**: Reduces the attack surface by not including unnecessary build tools in the final image.

### Key Changes:

- **`Stage 1 (Build Stage)`**: Installs the dependencies, but the final image won’t retain them.
- **`Stage 2 (Final Stage)`**: Copies only the necessary files from the build stage and includes the application code, resulting in a smaller final image.

>Note:

- The line COPY --from=build /app /app copies the entire /app directory from the build stage, but only the files that were explicitly copied into /app during the build stage are included.

- Since the requirements.txt and pip install commands were run only in the build stage, only the installed dependencies (which are located in /app or within virtual environments) are copied.

- Other intermediate files created during the build process (like cache files or temporary files) are not included, because they are outside the scope of what was explicitly copied to /app in the build stage.

- If you want to ensure that only specific files (e.g., the installed dependencies) are copied, you can specify those explicitly instead of copying the entire /app directory.

### Docker Image Build and Execution

```sh
rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker images
#REPOSITORY            TAG       IMAGE ID       CREATED       SIZE
#simple-python-image   latest    020ec9867f0f   4 hours ago   288MB
#jenkins/jenkins       lts       82a2134e1742   4 days ago    468MB
#atlassian/bitbucket   latest    d0dfcf14fed0   8 days ago    1.38GB

rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker ps -a
#CONTAINER ID   IMAGE                 COMMAND                  CREATED             STATUS                         PORTS     NAMES
#063f85c8ba19   simple-python-image   "python /app/ext_app…"   About an hour ago   Exited (0) About an hour ago             python-pandas-ext-container
#e6a4413d1b9d   atlassian/bitbucket   "/usr/bin/tini -- /e…"   2 days ago          Exited (143) 2 days ago                  bitbucket
#f8513221718e   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   3 days ago          Exited (143) 2 days ago                  jenkins

rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker build -t simple-python-multi-stage-image:latest .
#[+] Building 13.9s (11/11) FINISHED                                                                                                                                                                                                     docker:default
# => [internal] load build definition from dockerfile                                                                                                                                                                                              0.0s
# => => transferring dockerfile: 765B                                                                                                                                                                                                              0.0s
# => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                                                               1.1s
# => [internal] load .dockerignore                                                                                                                                                                                                                 0.0s
# => => transferring context: 2B                                                                                                                                                                                                                   0.0s
# => [internal] load build context                                                                                                                                                                                                                 0.0s
# => => transferring context: 63B                                                                                                                                                                                                                  0.0s
# => [build 1/4] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda                                                                                                                   0.0s
# => CACHED [build 2/4] WORKDIR /app                                                                                                                                                                                                               0.0s
# => CACHED [build 3/4] COPY requirements.txt .                                                                                                                                                                                                    0.0s
# => CACHED [build 4/4] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                                         0.0s
# => [stage-1 3/4] COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages                                                                                                                               5.7s
# => [stage-1 4/4] COPY app.py .                                                                                                                                                                                                                   0.1s
# => exporting to image                                                                                                                                                                                                                            1.4s
# => => exporting layers                                                                                                                                                                                                                           1.4s
# => => writing image sha256:5ce4a568460b546ff12ed23c165f4f21824dcaa088cedc5117cbf66e2d72de12                                                                                                                                                      0.0s
# => => naming to docker.io/library/simple-python-multi-stage-image:latest                                                                                                                                                                         0.0s

rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker images
#REPOSITORY                        TAG       IMAGE ID       CREATED          SIZE
#simple-python-multi-stage-image   latest    5ce4a568460b   20 seconds ago   294MB
#simple-python-image               latest    020ec9867f0f   4 hours ago      288MB
#jenkins/jenkins                   lts       82a2134e1742   4 days ago       468MB
#atlassian/bitbucket               latest    d0dfcf14fed0   8 days ago       1.38GB

rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker run --name python-pandas-multi-stage-image-container simple-python-multi-stage-image
#     name  cost
#0   apple    10
#1  banana     5
#2  orange     6

rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Containerization[Docker]/Multi_Stage_Single_Container_Deployment$ docker ps -a
#CONTAINER ID   IMAGE                             COMMAND                  CREATED             STATUS                         PORTS     NAMES
#aab00183d90d   simple-python-multi-stage-image   "python app.py"          9 seconds ago       Exited (0) 6 seconds ago                 python-pandas-multi-stage-image-container
#063f85c8ba19   simple-python-image               "python /app/ext_app…"   About an hour ago   Exited (0) About an hour ago             python-pandas-ext-container
#e6a4413d1b9d   atlassian/bitbucket               "/usr/bin/tini -- /e…"   2 days ago          Exited (143) 2 days ago                  bitbucket
#f8513221718e   jenkins/jenkins:lts               "/usr/bin/tini -- /u…"   3 days ago          Exited (143) 2 days ago                  jenkins
```