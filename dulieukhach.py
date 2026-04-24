import tkinter as tk
from tkinter import messagebox
import csv
import re
from datetime import datetime
import os

FILE_NAME = "khach_hang.csv"

#valid

def validate_name(name):
    return re.fullmatch(r"[A-Za-zÀ-ỹ\s]+", name) is not None

def validate_dob(dob):
    try:
        datetime.strptime(dob, "%d/%m/%Y")
        return True
    except:
        return False

def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None

#data

def insert_customer():
    name = entry_name.get().strip()
    dob = entry_dob.get().strip()
    address = entry_address.get().strip()
    phone = entry_phone.get().strip()

    if not validate_name(name):
        messagebox.showerror("Lỗi", "Tên không được chứa số hoặc ký tự đặc biệt")
        return

    if not validate_dob(dob):
        messagebox.showerror("Lỗi", "Ngày sinh phải đúng format dd/mm/yyyy")
        return

    if not validate_phone(phone):
        messagebox.showerror("Lỗi", "Số điện thoại phải gồm 10 chữ số")
        return

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Tên", "Ngày sinh", "Địa chỉ", "SĐT"])
        writer.writerow([name, dob, address, phone])

    messagebox.showinfo("Thành công", "Đã lưu thông tin khách hàng")


# search data

def search_customer():
    name = entry_name.get().strip()
    dob = entry_dob.get().strip()
    address = entry_address.get().strip()
    phone = entry_phone.get().strip()

    if not os.path.exists(FILE_NAME):
        messagebox.showerror("Lỗi", "Chưa có dữ liệu")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if (name and row["Tên"] == name) or \
               (dob and row["Ngày sinh"] == dob) or \
               (address and row["Địa chỉ"] == address) or \
               (phone and row["SĐT"] == phone):

                entry_name.delete(0, tk.END)
                entry_dob.delete(0, tk.END)
                entry_address.delete(0, tk.END)
                entry_phone.delete(0, tk.END)

                entry_name.insert(0, row["Tên"])
                entry_dob.insert(0, row["Ngày sinh"])
                entry_address.insert(0, row["Địa chỉ"])
                entry_phone.insert(0, row["SĐT"])

                return

    messagebox.showinfo("Kết quả", "Không tìm thấy khách hàng")


# GUI

root = tk.Tk()
root.title("Quản lý khách hàng")
root.geometry("400x250")

tk.Label(root, text="Tên").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Ngày sinh (dd/mm/yyyy)").grid(row=1, column=0, pady=5)
entry_dob = tk.Entry(root, width=30)
entry_dob.grid(row=1, column=1)

tk.Label(root, text="Địa chỉ").grid(row=2, column=0, pady=5)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=2, column=1)

tk.Label(root, text="Số điện thoại").grid(row=3, column=0, pady=5)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=3, column=1)

btn_insert = tk.Button(root, text="Nhập", command=insert_customer, width=10)
btn_insert.grid(row=4, column=0, pady=20)

btn_search = tk.Button(root, text="Tìm", command=search_customer, width=10)
btn_search.grid(row=4, column=1)

root.mainloop()