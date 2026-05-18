import sys


def solve():
    # Đọc toàn bộ đầu vào theo TỪNG DÒNG (splitlines)
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # Xóa bỏ các dòng trống (nếu có) để tránh lỗi
    lines = []
    for line in input_data:
        if line.strip() != '':
            lines.append(line.strip())

    n = int(lines[0])

    # 1. BƯỚC 1: Lập danh sách lớp (Giữ nguyên thứ tự gốc)
    danh_sach_sv = []
    idx = 1

    for _ in range(n):
        ma_sv = lines[idx]
        ho_ten = lines[idx + 1]
        lop = lines[idx + 2]

        # Gói 3 thông tin này vào 1 Dictionary nhỏ và cất vào List
        danh_sach_sv.append({
            'ma': ma_sv,
            'ten': ho_ten,
            'lop': lop
        })
        idx += 3

    # 2. BƯỚC 2: Thu thập sổ điểm danh
    # Dùng Dictionary để tra cứu siêu tốc: key là Mã SV, value là Chuỗi điểm danh
    so_diem_danh = {}
    for _ in range(n):
        # Dòng điểm danh có dạng: "B20DCCN001 xxxxmxxxvx"
        # Ta tách dòng này bằng khoảng trắng để lấy mã và chuỗi
        parts = lines[idx].split()
        ma = parts[0]
        chuoi = parts[1]

        so_diem_danh[ma] = chuoi
        idx += 1

    # 3. BƯỚC 3: Tính điểm và In kết quả
    # Đi dọc lại danh sách lớp ban đầu để đảm bảo in đúng thứ tự
    for sv in danh_sach_sv:
        ma_sv = sv['ma']
        # Mở sổ điểm danh ra tra mã sinh viên này
        chuoi_dd = so_diem_danh[ma_sv]

        # Bắt đầu tính điểm chuyên cần (Tối đa 10)
        diem = 10
        for ngay in chuoi_dd:
            if ngay == 'v':
                diem -= 2
            elif ngay == 'm':
                diem -= 1

        # Nếu trừ âm thì chốt lại thành 0
        if diem < 0:
            diem = 0

        # 4. IN KẾT QUẢ
        # Định dạng chuẩn: Mã Tên Lớp Điểm [Ghi chú]
        if diem == 0:
            print(f"{sv['ma']} {sv['ten']} {sv['lop']} {diem} KDDK")
        else:
            print(f"{sv['ma']} {sv['ten']} {sv['lop']} {diem}")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()