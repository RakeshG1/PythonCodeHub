import configparser
import yaml
from pathlib import Path

file_dir: str =  "/mnt/Local/Git_Repo/PythonCodeHub/Modules/" # Path.home()

# .ini parsing
config = configparser.ConfigParser()
config.read(file_dir+"config.ini")
print("config ini file_path -->", file_dir+"config.ini")
apple_host = config["DB:apple"]["hostname"]
print("Host:", apple_host)

# .yml parsing
with open(file_dir+"config.yml", "r") as f:
    config = yaml.safe_load(f)
print("config yml file_path -->", file_dir+"config.yml")
apple_host = config["DB"]["apple"]["hostname"]
print("Host:", apple_host)

# Output
#config ini file_path --> /mnt/Local/Git_Repo/PythonCodeHub/Modules/config.ini
#Host: abc
#config yml file_path --> /mnt/Local/Git_Repo/PythonCodeHub/Modules/config.yml
#Host: abc