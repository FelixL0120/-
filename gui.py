# /gui.py
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from model import ItemType, Item, User
from data import item_types
from data import load_item_types, add_item, load_users, save_users, register_user, approve_user

def create_register_gui():
    root = tk.Tk()
    root.title("用户注册")

    def register():
        username = username_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        response = register_user(username, email, address, phone)
        messagebox.showinfo("注册结果", response)
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

def create_add_item_gui():
    root = tk.Tk()
    root.title("添加物品")

    def add_item():
        item_type = item_type_var.get()
        name = name_entry.get()
        description = description_entry.get()
        address = address_entry.get()
        contact_phone = contact_phone_entry.get()
        email = email_entry.get()
        attributes = get_item_type_attributes(item_type)
        for attr, default in attributes.items():
            value = simpledialog.askstring(f"输入{attr}", f"{attr} ({default}):", parent=root)
            if value:
                attributes[attr] = value

        new_item = Item(item_type, name, description, address, contact_phone, email, **attributes)
        add_item(new_item)
        messagebox.showinfo("成功", "物品添加成功！")
        root.destroy()

    item_type_var = tk.StringVar()
    item_type_menu = tk.OptionMenu(root, item_type_var, *load_item_types().keys())
    item_type_menu.grid(row=0, column=1)

    tk.Label(root, text="物品名称:").grid(row=1, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1)

    # 其他输入框...

    tk.Button(root, text="添加物品", command=add_item).grid(row=10, column=1)

    root.mainloop()

def get_item_type_attributes(item_type_name):
    """
    根据物品类型的名称获取其属性。
    
    :param item_type_name: 物品类型的名称
    :return: 包含物品类型属性的字典
    """
    # 从全局 item_types 字典中获取物品类型对象
    item_type = item_types.get(item_type_name)
    if item_type:
        # 返回物品类型的属性字典
        return item_type.attributes
    else:
        # 如果物品类型不存在，返回空字典或错误信息
        return {}

if __name__ == "__main__":
    create_register_gui()
