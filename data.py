# /data.py

import json
from model import ItemType, Item

DATA_FILE = 'items.json'
USER_DATA_FILE = 'users.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(items):
    with open(DATA_FILE, 'w') as file:
        json.dump(items, file, indent=4)

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# 我们有以下物品类型数据结构
item_types = {
    "food": ItemType("food", {"expiration_date": "", "quantity": ""}),
    "book": ItemType("book", {"author": "", "publisher": ""})
}

def get_item_types():
    return item_types

def add_item_type(item_type):
    item_types[item_type.name] = item_type

def add_item(item):
    items = load_data()
    items[item.name] = item.__dict__
    save_data(items)
