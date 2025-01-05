# /gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from model import Item, ItemType
from data import load_item_types, add_item, load_users, save_users, approve_user

def create_register_gui():
    root = tk.Tk()
    root.title("用户注册")

    def register():
        username = username_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        # 这里应该添加逻辑来检查用户名是否已存在
        new_user = {username: {"email": email, "address": address, "phone": phone, "is_approved": False}}
        save_users(new_user)
        messagebox.showinfo("成功", "注册成功，等待管理员审批。")
        root.destroy()

    tk.Label(root, text="用户名:").grid(row=0, column=0)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1)

    tk.Label(root, text="邮箱:").grid(row=1, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1)

    tk.Label(root, text="地址:").grid(row=2, column=0)
    address_entry = tk.Entry(root)
    address_entry.grid(row=2, column=1)

    tk.Label(root, text="电话:").grid(row=3, column=0)
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=3, column=1)

    tk.Button(root, text="注册", command=register).grid(row=4, column=1)

    root.mainloop()

def create_admin_approve_gui():
    root = tk.Tk()
    root.title("管理员审批")

    def approve():
        username = username_entry.get()
        is_approved = approve_var.get()
        response = approve_user(username, is_approved)
        messagebox.showinfo("审批结果", response)
        root.destroy()

    users = load_users()
    user_listbox = tk.Listbox(root)
    for username in users:
        user_listbox.insert(tk.END, username)

    tk.Label(root, text="选择用户:").grid(row=0, column=0)
    tk.Label(root, text="审批状态:").grid(row=1, column=0)
    tk.Button(root, text="批准", command=lambda: approve(1)).grid(row=2, column=0)
    tk.Button(root, text="拒绝", command=lambda: approve(0)).grid(row=2, column=1)

    username_entry = tk.Entry(root)
    username_entry.grid(row=1, column=1)
    approve_var = tk.IntVar(value=1)  # 1 for approved, 0 for rejected

    user_listbox.grid(row=0, column=1)
    user_listbox.bind('<<ListboxSelect>>', lambda e: selected_user(e, username_entry))

    def selected_user(event, entry):
        selection = user_listbox.curselection()
        if selection:
            username = user_listbox.get(selection)
            entry.delete(0, tk.END)
            entry.insert(0, username)

    root.mainloop()

if __name__ == "__main__":
    create_register_gui()
