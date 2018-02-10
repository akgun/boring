import os
import json


def get_data_file(data_file):
    path = os.path.join(os.path.dirname(__file__), data_file)
    return path


def read_json_data_file(data_file):
    return json.load(open(get_data_file(data_file)))
