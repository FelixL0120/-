# users.py
from data import load_data, save_data
from model import User

class UserManager:
    def __init__(self):
        self.users = load_data(USERS_FILE)

    def add_user(self, user):
        self.users.append(user.__dict__)
        save_data(self.users, USERS_FILE)

    def authenticate(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None

    def approve_user(self, username):
        for user in self.users:
            if user['username'] == username:
                user['is_approved'] = True
                save_data(self.users, USERS_FILE)
                return True
        return False
