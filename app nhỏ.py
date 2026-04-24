import tkinter as tk
from tkinter import messagebox

def say_hello():
    name = entry_name.get().strip()
    if name == "":
        messagebox.showwarning("Canh bao", "Ban chua nhap ten")
        return
    lbl_result.config(text=f"Xin chao, {name}!")

root = tk.Tk()
root.title("Demo Tkinter")
root.geometry("1920x1080")

lbl_title = tk.Label(root, text="Nhap ten cua ban:", font=("Arial", 12))
lbl_title.pack(pady=10)

entry_name = tk.Entry(root, width=30, font=("Arial", 12))
entry_name.pack(pady=5)

btn = tk.Button(root, text="Chao toi", command=say_hello, font=("Arial", 11))
btn.pack(pady=10)

lbl_result = tk.Label(root, text="", fg="blue", font=("Arial", 12))
lbl_result.pack(pady=10)

root.mainloop()
