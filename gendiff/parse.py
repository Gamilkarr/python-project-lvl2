import json
import yaml


def open_file(file_path):
    extension = file_path.split(".")[-1]
    with open(file_path) as f:
        if extension == "json":
            file = json.load(f)
        elif extension == "yaml" or extension == "yml":
            file = yaml.safe_load(f)
    return file
