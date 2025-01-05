def create_gui():
    root = tk.Tk()
    root.title("物品复活软件")

    def add_item_interface():
        # 弹出对话框让用户输入物品信息
        name = simpledialog.askstring("输入", "物品名称:")
        description = simpledialog.askstring("输入", "物品描述:")
        address = simpledialog.askstring("输入", "物品地址:")
        contact_phone = simpledialog.askstring("输入", "联系人手机:")
        email = simpledialog.askstring("输入", "邮箱:")
        item_type = simpledialog.askstring("输入", "物品类型:")

        # 根据选择的物品类型获取属性
        attributes = get_item_types()[item_type].attributes
        for attr, default in attributes.items():
            value = simpledialog.askstring(f"输入{attr}", f"{attr} ({default}):")
            attributes[attr] = value

        # 创建物品并添加到数据中
        new_item = Item(item_type, name, description, address, contact_phone, email, **attributes)
        add_item(new_item)
        messagebox.showinfo("成功", "物品添加成功！")

    # 添加物品按钮
    add_button = tk.Button(root, text="添加物品", command=add_item_interface)
    add_button.pack()

    root.mainloop()

def create_register_gui():
    root = tk.Tk()
    root.title("用户注册")

    def register():
        username = username_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        new_user = User(username, email, address, phone)
        register_user(new_user)
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

if __name__ == "__main__":
    create_gui()

    # 列表框
    listbox = tk.Listbox(root)
    listbox.grid(row=5, column=0, columnspan=2)

    root.mainloop()
