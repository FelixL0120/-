# /data.py

import json
from model import ItemType, Item

DATA_FILE = 'items.json'
USER_DATA_FILE = 'users.json'
ITEM_TYPES_FILE = 'item_types.json'

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def load_items():
    return load_data(DATA_FILE)

def load_users():
    return load_data(USER_DATA_FILE)

def load_item_types():
    return load_data(ITEM_TYPES_FILE)

def save_items(items):
    save_data(items, DATA_FILE)

def save_users(users):
    save_data(users, USER_DATA_FILE)

def save_item_types(item_types):
    save_data(item_types, ITEM_TYPES_FILE)

item_types = {
    "food": ItemType("food", {"expiration_date": "", "quantity": ""}),
    "book": ItemType("book", {"author": "", "publisher": ""}),
    "tool": ItemType("tool", {"brand": "", "model": ""})
}

def add_item_type(item_type):
    item_types[item_type.name] = item_type
    save_item_types(item_types)

def add_item(item):
    items = load_items()
    items[item.name] = item.__dict__
    save_items(items)
