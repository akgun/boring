import os


def getdatafile(data_file):
    path = os.path.join(os.path.dirname(__file__), data_file)
    return path