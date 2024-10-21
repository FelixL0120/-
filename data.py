import json

DATA_FILE = 'items.json'

def load_items():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_items(items):
    with open(DATA_FILE, 'w') as file:
        json.dump(items, file, indent=4)

def add_item(items, name, description, contact):
    if name in items:
        return False, "物品已存在。"
    items[name] = {
        'description': description,
        'contact': contact
    }
    return True, "物品添加成功。"

def remove_item(items, name):
    if name in items:
        del items[name]
        return True, "物品删除成功。"
    return False, "物品不存在。"

def find_item(items, name):
    if name in items:
        info = items[name]
        return True, f"{name}: {info['description']}, 联系人: {info['contact']}"
    return False, "物品不存在。"
