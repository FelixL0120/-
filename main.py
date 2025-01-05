# /main.py

import tkinter as tk
from gui import create_register_gui, create_admin_approve_gui, create_add_item_gui

def main():
    # 创建主窗口
    root = tk.Tk()
    root.title("物品复活软件")

    def switch_to_register():
        # 切换到用户注册界面
        root.destroy()
        create_register_gui()

    def switch_to_admin_approve():
        # 切换到管理员审批界面
        root.destroy()
        create_admin_approve_gui()

    def switch_to_add_item():
        # 切换到添加物品界面
        root.destroy()
        create_add_item_gui()

    # 创建主界面的按钮
    tk.Button(root, text="用户注册", command=switch_to_register).pack(fill=tk.X)
    tk.Button(root, text="管理员审批", command=switch_to_admin_approve).pack(fill=tk.X)
    tk.Button(root, text="添加物品", command=switch_to_add_item).pack(fill=tk.X)

    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    main()
