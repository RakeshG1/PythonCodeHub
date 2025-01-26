## Create the Engine Package

```md
* engine/
* │
  * ├── engine.py
  * ├── __init__.py
  * └── pyproject.toml
```

* **engine.py**: Contains your engine logic.
* **__init__.py**: An empty file (or can have code) indicating my_engine is a package.
* **pyproject.toml**: The Poetry configuration file for building/installing.

## Build the Engine Package

Inside the engine folder, run:

```sh
poetry build
```

This generates a dist/ folder containing .whl and/or .tar.gz files for my_engine.

**`Execution`**
```sh
(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ ls -la
total 5
drwxrwxrwx 1 root root    0 Jan 26 19:04 .
drwxrwxrwx 1 root root 4096 Jan 26 19:09 ..
drwxrwxrwx 1 root root    0 Jan 26 19:06 engine
-rwxrwxrwx 1 root root  499 Jan 26 19:09 README.md

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ cd engine/

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module/engine$ poetry build
Building engine (0.1.0)
  - Building sdist
  - Built engine-0.1.0.tar.gz
  - Building wheel
  - Built engine-0.1.0-py3-none-any.whl

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module/engine$ ls -la
total 2
drwxrwxrwx 1 root root   0 Jan 26 19:10 .
drwxrwxrwx 1 root root   0 Jan 26 19:04 ..
drwxrwxrwx 1 root root   0 Jan 26 19:10 dist
-rwxrwxrwx 1 root root  49 Jan 26 19:05 engine.py
-rwxrwxrwx 1 root root  80 Jan 26 19:05 __init__.py
-rwxrwxrwx 1 root root 283 Jan 26 19:06 pyproject.toml
```


## Install Engine Module

```sh
(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ nano ../pyproject.toml 

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ cat ../pyproject.toml 
[tool.poetry]
name = "pythoncodehub"
version = "0.1.0"
description = ""
authors = ["None"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
logging = "*"
engine = {path = "Module/engine"}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ poetry install
Installing dependencies from lock file

pyproject.toml changed significantly since poetry.lock was last generated. Run `poetry lock [--no-update]` to fix the lock file.

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ poetry lock
Updating dependencies
Resolving dependencies... (0.6s)

Writing lock file

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ poetry install
Installing dependencies from lock file

Package operations: 1 install, 0 updates, 0 removals

  - Installing engine (0.1.0 /mnt/Local/Git_Repo/PythonCodeHub/Module/engine)

Installing the current project: pythoncodehub (0.1.0)
Warning: The current project could not be installed: No file/folder found for package pythoncodehub
If you do not want to install the current project use --no-root.
If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
In a future version of Poetry this warning will become an error!
```

## Import Module

**`Execution`**

```sh
(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ ls -la
total 6
drwxrwxrwx 1 root root    0 Jan 26 19:11 .
drwxrwxrwx 1 root root 4096 Jan 26 19:22 ..
-rwxrwxrwx 1 root root   67 Jan 26 19:12 Car.py
drwxrwxrwx 1 root root    0 Jan 26 19:10 engine
-rwxrwxrwx 1 root root 1500 Jan 26 19:11 README.md

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub/Module$ python Car.py 
Engine Started
```