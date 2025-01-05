# /data.py
# src/data.py

import json
from model import ItemType, Item, User

# 文件路径
DATA_FILE = 'items.json'
USER_DATA_FILE = 'users.json'
ITEM_TYPES_FILE = 'item_types.json'

def load_data(file_path):
    """加载数据文件"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data, file_path):
    """保存数据到文件"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_items():
    """加载物品数据"""
    return load_data(DATA_FILE)

def save_items(items):
    """保存物品数据"""
    save_data(items, DATA_FILE)

def load_users():
    """加载用户数据"""
    return load_data(USER_DATA_FILE)

def save_users(users):
    """保存用户数据"""
    save_data(users, USER_DATA_FILE)

def load_item_types():
    """加载物品类型数据"""
    return load_data(ITEM_TYPES_FILE)

def save_item_types(item_types):
    """保存物品类型数据"""
    save_data(item_types, ITEM_TYPES_FILE)

def add_item_type(item_type):
    """添加新的物品类型"""
    item_types = load_item_types()
    item_types[item_type.name] = item_type.__dict__
    save_item_types(item_types)

def add_item(item):
    """添加新的物品"""
    items = load_items()
    items[item.name] = item.__dict__
    save_items(items)

def register_user(new_user):
    """注册新用户"""
    users = load_users()
    if new_user.username in users:
        return "用户名已存在。"
    users[new_user.username] = new_user.__dict__
    save_users(users)
    return "用户注册成功，等待管理员审批。"

def approve_user(username, is_approved):
    """管理员审批用户"""
    users = load_users()
    if username not in users:
        return "用户不存在。"
    users[username]['is_approved'] = is_approved
    save_users(users)
    return "用户审批成功。"

# 初始化物品类型
def initialize_data():
    item_types = {
        "food": ItemType("food", {"expiration_date": "", "quantity": ""}),
        "book": ItemType("book", {"author": "", "publisher": ""}),
        "tool": ItemType("tool", {"brand": "", "model": ""})
    }
    save_item_types(item_types)

# 检查数据文件是否存在，如果不存在则初始化
if not (load_items() or load_users() or load_item_types()):
    initialize_data()
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
