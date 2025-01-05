# /users.py

from model import User
from data import load_users, save_users

def register_user(username, email, address, phone, is_admin=False):
    """
    注册新用户。
    
    :param username: 用户名
    :param email: 邮箱
    :param address: 地址
    :param phone: 电话
    :param is_admin: 是否为管理员，默认为False
    :return: 注册结果信息
    """
    users = load_users()
    if username in users:
        return "用户名已存在。"
    new_user = User(username, email, address, phone, is_admin=is_admin)
    users[username] = new_user.__dict__
    save_users(users)
    return "用户注册成功，等待管理员审批。"

def approve_user(username, is_approved):
    """
    管理员审批用户。
    
    :param username: 用户名
    :param is_approved: 是否审批通过
    :return: 审批结果信息
    """
    users = load_users()
    if username not in users:
        return "用户不存在。"
    users[username]['is_approved'] = is_approved
    save_users(users)
    return "用户审批成功。"

def login_user(username, password):
    """
    用户登录。
    
    :param username: 用户名
    :param password: 密码
    :return: 登录结果信息
    """
    # 注意：这里的密码验证是非常基础的，实际应用中应该使用加密存储和验证
    users = load_users()
    if username in users and users[username]['password'] == password:
        return "登录成功。"
    return "用户名或密码错误。"

def change_user_password(username, old_password, new_password):
    """
    更改用户密码。
    
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return: 密码更改结果信息
    """
    users = load_users()
    if username in users and users[username]['password'] == old_password:
        users[username]['password'] = new_password
        save_users(users)
        return "密码更改成功。"
    return "旧密码错误或用户不存在。"

if __name__ == "__main__":
    users = {
        "admin": {"email": "admin@example.com", "address": "Admin Street", "phone": "1234567890", "is_approved": True, "is_admin": True, "password": "adminpass"}
    }
    save_users(users)
