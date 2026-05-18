import sys


def solve():
    # 1. Đọc toàn bộ đầu vào theo từng dòng để bảo toàn các khoảng trắng trong Tên
    input_data = sys.stdin.read().splitlines()

    # Lọc bỏ các dòng trống rỗng (do lỗi gõ phím hoặc format của hệ thống chấm)
    lines = [line.strip() for line in input_data if line.strip() != '']

    if not lines:
        return

    so_luong_hoa_don = int(lines[0])
    idx = 1

    # "Rổ" chứa các hóa đơn
    danh_sach_hoa_don = []

    # 2. XỬ LÝ TỪNG HÓA ĐƠN
    for _ in range(so_luong_hoa_don):
        ma_hang = lines[idx]
        ten_hang = lines[idx + 1]
        so_luong = int(lines[idx + 2])  # Nhớ ép kiểu số nguyên để tính toán
        don_gia = int(lines[idx + 3])
        chiet_khau = int(lines[idx + 4])
        idx += 5

        # Tính tổng tiền khách phải trả
        tong_tien = (don_gia * so_luong) - chiet_khau

        # Đóng gói 6 thông tin vào một cuốn từ điển (Dictionary)
        danh_sach_hoa_don.append({
            'ma': ma_hang,
            'ten': ten_hang,
            'so_luong': so_luong,
            'don_gia': don_gia,
            'chiet_khau': chiet_khau,
            'tong_tien': tong_tien
        })

    # 3. SẮP XẾP DANH SÁCH
    # Yêu cầu: Sắp xếp theo số tiền giảm dần
    # Dùng reverse=True để lật ngược thứ tự từ Lớn xuống Bé
    danh_sach_hoa_don.sort(key=lambda x: x['tong_tien'], reverse=True)

    # 4. IN KẾT QUẢ
    for hd in danh_sach_hoa_don:
        # Sử dụng f-string để nối các thông tin lại bằng một khoảng trắng
        print(f"{hd['ma']} {hd['ten']} {hd['so_luong']} {hd['don_gia']} {hd['chiet_khau']} {hd['tong_tien']}")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()