import json
import numpy

def read_json_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def write_json_file(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# %load_ext autoreload
# %autoreload 2