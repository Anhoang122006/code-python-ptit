import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry.get()
    messagebox.showinfo("Thông báo", f"Xin chào {name}")

root = tk.Tk()
root.title("Demo")
root.geometry("300x200")

tk.Label(root, text="Nhập tên:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()
