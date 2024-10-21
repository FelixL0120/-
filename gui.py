import tkinter as tk
from tkinter import messagebox
from data import load_items, save_items, add_item, remove_item, find_item

def create_gui():
    root = tk.Tk()
    root.title("物品复活软件")

    items = load_items()

    def add_item_to_list():
        _, message = add_item(items, name_entry.get(), description_entry.get(), contact_entry.get())
        messagebox.showinfo("信息", message)
        list_items()

    def remove_item_from_list():
        _, message = remove_item(items, name_entry.get())
        messagebox.showinfo("信息", message)
        list_items()

    def list_items():
        listbox.delete(0, tk.END)
        for name, info in items.items():
            listbox.insert(tk.END, f"{name}: {info['description']}, 联系人: {info['contact']}")

    def find_item_in_list():
        _, message = find_item(items, name_entry.get())
        messagebox.showinfo("信息", message)

    # 输入框标签和输入框
    tk.Label(root, text="物品名称:").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="物品描述:").grid(row=1, column=0)
    description_entry = tk.Entry(root)
    description_entry.grid(row=1, column=1)

    tk.Label(root, text="联系人信息:").grid(row=2, column=0)
    contact_entry = tk.Entry(root)
    contact_entry.grid(row=2, column=1)

    # 按钮
    tk.Button(root, text="添加物品", command=add_item_to_list).grid(row=3, column=0)
    tk.Button(root, text="删除物品", command=remove_item_from_list).grid(row=3, column=1)
    tk.Button(root, text="显示物品列表", command=list_items).grid(row=4, column=0)
    tk.Button(root, text="查找物品", command=find_item_in_list).grid(row=4, column=1)

    # 列表框
    listbox = tk.Listbox(root)
    listbox.grid(row=5, column=0, columnspan=2)

    root.mainloop()
