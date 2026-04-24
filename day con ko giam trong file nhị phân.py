def la_so_khong_giam(n):
    s = str(n)
    # Số phải có ít nhất 2 chữ số theo đề bài
    if len(s) < 2:
        return False
    # Kiểm tra chữ số sau có nhỏ hơn chữ số trước không
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True

def solve():
    # Giả sử ta có danh sách số từ file 1 và file 2
    # Ở đây thầy hướng dẫn cách xử lý logic đếm và so khớp
    list1 = [59, 66, 1228, 59, 66] # Ví dụ dữ liệu file 1
    list2 = [59, 1228, 66, 1228]   # Ví dụ dữ liệu file 2

    # Tìm các số không giảm xuất hiện ở cả 2 danh sách
    ket_qua = {}
    for x in list1:
        if la_so_khong_giam(x) and (x in list2):
            if x not in ket_qua:
                # Lưu [số_lần_f1, số_lần_f2]
                ket_qua[x] = [list1.count(x), list2.count(x)]

    # Sắp xếp các số tăng dần để in ra
    cac_so = sorted(ket_qua.keys())
    for x in cac_so:
        counts = ket_qua[x]
        print(f"{x} {counts[0]} {counts[1]}")

# solve() # Em có thể chạy thử với dữ liệu mẫu
