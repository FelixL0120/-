# /users.py

from model import User
from data import load_users, save_users

def register_user(username, email, address, phone):
    users = load_users()
    if username in users:
        return "用户名已存在。"
    new_user = User(username, email, address, phone)
    users[username] = new_user.__dict__
    save_users(users)
    return "用户注册成功，等待管理员审批。"

def approve_user(username, is_approved):
    users = load_users()
    if username in users:
        users[username]['is_approved'] = is_approved
        save_users(users)
        return "用户审批成功。"
    return "用户不存在。"
