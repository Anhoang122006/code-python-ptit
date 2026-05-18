import sys


def solve():
    # 1. Đọc toàn bộ dữ liệu đầu vào theo từng dòng
    input_data = sys.stdin.read().splitlines()

    # Lọc bỏ các dòng trống rỗng nếu có
    lines = [line.strip() for line in input_data if line.strip() != ""]

    if not lines:
        return

    # Dòng đầu tiên là số lượng môn học N
    n = int(lines[0])
    idx = 1

    danh_sach_mon = []

    # 2. GOM NHÓM THÔNG TIN
    # Mỗi môn học chiếm đúng 3 dòng tiếp theo
    for _ in range(n):
        ma_mon = lines[idx]
        ten_mon = lines[idx + 1]
        hinh_thuc = lines[idx + 2]

        # Gói vào một Dictionary
        mon_hoc = {
            'ma': ma_mon,
            'ten': ten_mon,
            'hinh_thuc': hinh_thuc
        }
        danh_sach_mon.append(mon_hoc)
        idx += 3

    # 3. SẮP XẾP THEO MÃ MÔN (Thứ tự từ điển tăng dần)
    # Python mặc định sắp xếp chuỗi theo thứ tự A-Z
    danh_sach_mon.sort(key=lambda x: x['ma'])

    # 4. IN KẾT QUẢ
    for m in danh_sach_mon:
        # Nối các thông tin bằng khoảng trắng
        print(f"{m['ma']} {m['ten']} {m['hinh_thuc']}")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()