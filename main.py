# main.py
import tkinter as tk
from users import UserManager
from gui import App

if __name__ == "__main__":
    root = tk.Tk()
    user_manager = UserManager()
    app = App(root, user_manager)
    root.mainloop()
