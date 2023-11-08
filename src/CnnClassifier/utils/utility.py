import os
import sys
import yaml
import json
import joblib
import base64
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations

from CnnClassifier.logger import logging
from CnnClassifier.exception import CustomExceptionHandling


@ensure_annotations
def load_yaml(path_to_yaml_file: Path) -> ConfigBox:
    ''' Reads yaml files

    Args :
        path_to_yaml_file : Path like input

    Returns :
        ConfigBox: ConfigBox type
    '''
    try:
        with open(path_to_yaml_file) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info("{path_to_yaml_file} yaml file loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomExceptionHandling(e, sys)


@ensure_annotations
def create_directories(path_to_dirs: list, ignore_log=True):
    ''' Creates directories

    Args :
        path_to_dirs : list of directories
        ignore_log : Set to False when multiple directories needs to be created
    '''
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if (not ignore_log):
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_as_json(path: Path, data: dict):
    '''Save data in json files

    Args :
        path : path to json file
        data : dictionary data to be saved 
    '''
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logging.info(f"Json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    ''' Reads json file

    Args :
        path : path to json file

    Returns :
        ConfigBox: ConfigBox type
    '''
    with open(path) as f:
        content = json.load(f)

    logging.info(f"Data read from Json file at {path}")
    return ConfigBox(content)


@ensure_annotations
def save_as_bin(path: Path, data):
    '''Save data as binary files

    Args :
        path : path to json file
        data : Any data to be saved 
    '''
    joblib.dump(value=data, filename=path)
    logging.info(f"Joblib file saved at {path}")


@ensure_annotations
@
def load_binary(path: Path) :
    ''' Reads binary file

    Args :
        path : path to binary file

    Returns :
        Any : Any data type
    '''
    content = joblib.load(path)
    logging.info(f"Data read from joblib file at {path}")
    return content


# def get_size in KB

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

