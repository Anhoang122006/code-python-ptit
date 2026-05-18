import sys


def solve():
    # 1. Đọc dữ liệu an toàn theo từng dòng (bỏ qua dòng trống)
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip() != '']

    if not lines:
        return

    n = int(lines[0])
    idx = 1

    danh_sach_gv = []

    # 2. Tạo 2 cuốn "từ điển" tra cứu siêu tốc (tránh dùng if-else quá dài)
    tu_dien_mon = {
        'A': 'TOÁN',
        'B': 'LÝ',
        'C': 'HÓA'
    }

    tu_dien_uu_tien = {
        '1': 2.0,
        '2': 1.5,
        '3': 1.0,
        '4': 0.0
    }

    # 3. XỬ LÝ TỪNG ỨNG VIÊN
    for i in range(1, n + 1):
        ten = lines[idx]
        ma_xt = lines[idx + 1]
        diem_tin = float(lines[idx + 2])  # Nhớ ép kiểu float vì điểm có số thập phân
        diem_cm = float(lines[idx + 3])
        idx += 4

        # Sinh mã giáo viên tự động
        ma_gv = f"GV{i:02d}"

        # Tách mã xét tuyển (Ký tự đầu là Môn, ký tự sau là Ưu tiên)
        ma_mon = ma_xt[0]
        ma_uu_tien = ma_xt[1]

        # Tra từ điển để lấy kết quả
        ten_mon = tu_dien_mon[ma_mon]
        diem_ut = tu_dien_uu_tien[ma_uu_tien]

        # Tính tổng điểm (Tin học nhân đôi)
        tong_diem = diem_tin * 2 + diem_cm + diem_ut

        # Xác định trạng thái
        if tong_diem >= 18:
            trang_thai = "TRÚNG TUYỂN"
        else:
            trang_thai = "LOẠI"

        # Lưu hồ sơ vào danh sách
        danh_sach_gv.append({
            'ma': ma_gv,
            'ten': ten,
            'mon': ten_mon,
            'tong': tong_diem,
            'trang_thai': trang_thai
        })

    # 4. SẮP XẾP DANH SÁCH
    # Ưu tiên 1: Tổng điểm giảm dần (-x['tong'])
    # Ưu tiên 2: Mã GV tăng dần (x['ma']) - Tránh trường hợp bằng điểm nhau
    danh_sach_gv.sort(key=lambda x: (-x['tong'], x['ma']))

    # 5. IN KẾT QUẢ
    for gv in danh_sach_gv:
        # {gv['tong']:.1f} giúp định dạng in ra đúng 1 chữ số thập phân (VD: 18.0)
        print(f"{gv['ma']} {gv['ten']} {gv['mon']} {gv['tong']:.1f} {gv['trang_thai']}")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()