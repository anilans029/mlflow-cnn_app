import yaml
import os
import zipfile
import io


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


def log_model_summary(model):
    with io.StringIO() as stream:
        model.summary(
            print_fn=lambda x: stream.write(f"{x}\n")
        )
        summary_str = stream.getvalue()
    return summary_str
