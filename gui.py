# gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from users import UserManager
from data import load_data
from model import User, Item, ItemType

class App:
    def __init__(self, root, user_manager):
        self.root = root
        self.user_manager = user_manager
        self.current_user = None

        self.root.title("物品复活系统")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="用户名:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="密码:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_frame, text="登录", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self.login_frame, text="注册", command=self.register).grid(row=3, column=0, columnspan=2)
        tk.Button(self.login_frame, text="注册管理员", command=self.register_admin).grid(row=4, column=0, columnspan=2)

    def register_admin(self):
        username = simpledialog.askstring("注册管理员", "请输入用户名:")
        password = simpledialog.askstring("注册管理员", "请输入密码:", show="*")
        address = simpledialog.askstring("注册管理员", "请输入地址:")
        contact = simpledialog.askstring("注册管理员", "请输入联系方式:")

        if username and password and address and contact:
            if self.user_manager.register_admin(username, password, address, contact):
                messagebox.showinfo("注册成功", "管理员账户注册成功")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.user_manager.authenticate(username, password)
        if user:
            if not user['is_approved']:
                messagebox.showerror("登录失败", "用户未被批准")
                return
            self.current_user = user
            self.login_frame.destroy()
            self.create_main_widgets()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误")

    def register(self):
        username = simpledialog.askstring("注册", "请输入用户名:")
        password = simpledialog.askstring("注册", "请输入密码:", show="*")
        address = simpledialog.askstring("注册", "请输入地址:")
        contact = simpledialog.askstring("注册", "请输入联系方式:")
        is_admin = False

        if username and password and address and contact:
            user = User(username, password, address, contact, is_admin)
            self.user_manager.add_user(user)
            messagebox.showinfo("注册成功", "请等待管理员批准")

    def create_main_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        if self.current_user['is_admin']:
            tk.Button(self.main_frame, text="批准用户", command=self.approve_users).grid(row=0, column=0)

        # 其他功能按钮可以在这里添加

    def approve_users(self):
        for user in self.user_manager.users:
            if not user['is_approved']:
                if messagebox.askyesno("批准用户", f"是否批准用户 {user['username']}?"):
                    self.user_manager.approve_user(user['username'])
