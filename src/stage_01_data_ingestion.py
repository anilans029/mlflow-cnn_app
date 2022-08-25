import argparse
import urllib.request as req
from venv import create
from src.utils.utils import read_yaml,create_directories, unzip_file
import os
from src.logger import logging


def main(config):

    config_file= read_yaml(config)  
    dataset_url = config_file["data"]["source_url"]
    sorce_data_dir = os.path.join(config_file["data"]["data_dir"],config_file["data"]["source_zipped_data_dir"])
    extracted_data_dir = os.path.join(config_file["data"]["data_dir"],config_file["data"]["unzip_data_dir"])

    sorce_data_file_name  = config_file["data"]["source_filename"]
    extracted_data_parent_dir = os.path.join(extracted_data_dir, config_file["data"]["parent_data_dir"])
    file_path = os.path.join(sorce_data_dir, sorce_data_file_name)

    create_directories([sorce_data_dir])
    create_directories([extracted_data_dir])


    if not os.path.exists(file_path):
        logging.info("dataset download started")
        filename, headers = req.urlretrieve(dataset_url,file_path)
        logging.info("dataset download completed")
    else:
        logging.info(f"data already present at {file_path}")

    if not os.path.exists(extracted_data_parent_dir):
        logging.info("dataset extraction started")
        unzip_file(file_path,extracted_data_dir )
        logging.info("dataset extraction completed")
    else:
        logging.info(f"data already extracted at {extracted_data_dir}")
    
    

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")



    parsed_args = args.parse_args()
    main(parsed_args.config)