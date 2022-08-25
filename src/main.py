import mlflow
import argparse
import os
from src.logger import logging
from src.utils.utils import read_yaml, create_directories


STAGE = "MAIN" ## <<< change stage name 



def main():
    with mlflow.start_run() as run:
        mlflow.run(".", "get_data", use_conda=False)
        # mlflow.run(".", "get_data", parameters={}, use_conda=False)
        mlflow.run(".", "base_model_creation", use_conda=False)
        mlflow.run(".", "training", use_conda=False)

if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
