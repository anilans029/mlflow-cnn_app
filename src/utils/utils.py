import yaml
import os
import zipfile

def read_yaml(file_path:str):
    with open(file_path) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directories(directories:list):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def unzip_file(file:str, destinationPath: str):
    with zipfile.ZipFile(file,"r") as file:
        file.extractall(destinationPath)
