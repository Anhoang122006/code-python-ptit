import sys


def solve():
    # 1. Đọc toàn bộ đầu vào (bỏ qua việc xuống dòng hay khoảng trắng lộn xộn)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    # 2. Lấy danh sách các con số (các bạn đang có mặt)
    a = []
    for i in range(1, N + 1):
        a.append(int(input_data[i]))

    # Tìm số thứ tự lớn nhất trong lớp
    max_val = max(a)

    # Biến danh sách thành 'set' (tập hợp) để kiểm tra sự tồn tại siêu tốc
    a_set = set(a)

    # Tạo một chiếc giỏ rỗng để chứa các số bị đánh rơi
    danh_sach_roi = []

    # 3. Quá trình điểm danh (đếm từ 1 đến max_val)
    for i in range(1, max_val + 1):
        if i not in a_set:  # Nếu số i KHÔNG CÓ mặt trong lớp
            danh_sach_roi.append(i)  # Đưa vào sổ bìa đen

    # 4. Thông báo kết quả
    if len(danh_sach_roi) == 0:
        print("Excellent!")
    else:
        for so in danh_sach_roi:
            print(so)


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()