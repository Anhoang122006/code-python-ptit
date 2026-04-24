import tkinter as tk

# ================== HÀM XỬ LÝ ==================

def click(button_value):
    """
    Hàm được gọi khi bấm nút
    button_value: giá trị của nút (số, +, -, ...)
    """
    current = entry.get()              # lấy nội dung hiện tại
    entry.delete(0, tk.END)            # xóa ô nhập
    entry.insert(0, current + button_value)  # thêm ký tự mới


def clear():
    """Xóa toàn bộ màn hình"""
    entry.delete(0, tk.END)


def calculate():
    """Tính toán kết quả"""
    try:
        expression = entry.get()       # lấy biểu thức (vd: 2+3*5)
        result = eval(expression)      # tính toán
        entry.delete(0, tk.END)
        entry.insert(0, str(result))   # hiển thị kết quả
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")       # nếu sai cú pháp


# ================== GIAO DIỆN ==================

root = tk.Tk()
root.title("Máy tính GUI")
root.geometry("300x400")

# Ô hiển thị (Entry)
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ================== TẠO NÚT ==================

# Danh sách các nút
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for b in buttons:
    # Nếu là nút C (clear)
    if b == 'C':
        action = clear
    # Nếu là nút =
    elif b == '=':
        action = calculate
    else:
        # dùng lambda để truyền giá trị nút vào hàm click
        action = lambda x=b: click(x)

    # Tạo nút
    tk.Button(root,
              text=b,
              width=5,
              height=2,
              font=("Arial", 14),
              command=action
              ).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    # xuống dòng sau 4 nút
    if col > 3:
        col = 0
        row += 1


# ================== CHẠY APP ==================
root.mainloop()
