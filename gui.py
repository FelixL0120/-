# /gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from model import Item, ItemType
from data import load_item_types, add_item, load_items, add_item_type

def create_gui():
    root = tk.Tk()
    root.title("物品复活软件")

    def add_item_interface():
        name = simpledialog.askstring("输入", "物品名称:")
        description = simpledialog.askstring("输入", "物品描述:")
        address = simpledialog.askstring("输入", "物品地址:")
        contact_phone = simpledialog.askstring("输入", "联系人手机:")
        email = simpledialog.askstring("输入", "邮箱:")
        item_type = simpledialog.askstring("输入", "物品类型:")

        attributes = load_item_types()[item_type].attributes
        for attr, default in attributes.items():
            value = simpledialog.askstring(f"输入{attr}", f"{attr} ({default}):")
            attributes[attr] = value

        new_item = Item(item_type, name, description, address, contact_phone, email, **attributes)
        add_item(new_item)
        messagebox.showinfo("成功", "物品添加成功！")

    add_button = tk.Button(root, text="添加物品", command=add_item_interface)
    add_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
