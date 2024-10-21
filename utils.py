import tkinter as tk

def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)
