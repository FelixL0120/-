# data.py
import json
import os

DATA_FILE = 'items.json'
USERS_FILE = 'users.json'
TYPES_FILE = 'types.json'

def load_data(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)
    with open(file, 'r') as f:
        return json.load(f)

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
