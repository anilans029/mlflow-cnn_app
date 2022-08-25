from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = " "
AUTHOR_USER_NAME = "anilans029"
SRC_REPO = "src"
REQUIREMENTS_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """
    The get_requirements_list function returns a list of all the packages in the requirements file.
    :return: A list of strings that contain the contents of the requirements
    :author: anil
    """
  
    with open(REQUIREMENTS_FILE_NAME,"r") as requriemets:
        return requriemets.readlines().remove("-e .")

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for MLflow app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="anilsai029@gmail.com",
    packages= find_packages(),
    license="MIT",
    python_requires=">=3.6",
    install_requires=get_requirements_list()
)
