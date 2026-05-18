import sys
# Phải gọi thư viện datetime để Python biết cách trừ ngày tháng
from datetime import datetime


def solve():
    # 1. Đọc dữ liệu an toàn theo từng dòng
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # Lọc bỏ các dòng trắng rác (nếu có)
    lines = []
    for line in input_data:
        if line.strip() != '':
            lines.append(line.strip())

    n = int(lines[0])
    idx = 1

    # Cuốn sổ lưu thông tin toàn bộ khách hàng
    danh_sach_kh = []

    # Bảng giá phòng tra cứu nhanh (Dictionary)
    gia_tang = {
        '1': 25,
        '2': 34,
        '3': 50,
        '4': 80
    }

    # 2. XỬ LÝ TỪNG KHÁCH HÀNG
    for i in range(1, n + 1):
        ten = lines[idx]
        phong = lines[idx + 1]
        ngay_nhan_str = lines[idx + 2]
        ngay_tra_str = lines[idx + 3]
        tien_dich_vu = int(lines[idx + 4])
        idx += 5

        # Sinh mã khách hàng tự động
        ma_kh = f"KH{i:02d}"

        # Quy đổi chuỗi văn bản thành Thời gian thật
        # "%d/%m/%Y" là mẫu cho biết thứ tự: Ngày/Tháng/Năm_4_số
        ngay_nhan = datetime.strptime(ngay_nhan_str, "%d/%m/%Y")
        ngay_tra = datetime.strptime(ngay_tra_str, "%d/%m/%Y")

        # Tính số ngày ở.
        # .days giúp trích xuất số ngày từ kết quả phép trừ
        # Cộng thêm 1 vì quy định thường thấy (ở và đi trong cùng 1 ngày = 1 ngày)
        so_ngay = (ngay_tra - ngay_nhan).days + 1

        # Tính tiền phòng dựa vào tầng
        tang = phong[0]  # Lấy ký tự đầu tiên
        gia_mot_ngay = gia_tang[tang]

        tong_tien = (so_ngay * gia_mot_ngay) + tien_dich_vu

        # Gói vào một thẻ hồ sơ (Dictionary) và nhét vào rổ
        danh_sach_kh.append({
            'ma': ma_kh,
            'ten': ten,
            'phong': phong,
            'so_ngay': so_ngay,
            'tong_tien': tong_tien
        })

    # 3. SẮP XẾP
    # Cú pháp cực mạnh: Xếp danh sách dựa theo ('key') giá trị 'tong_tien'.
    # reverse=True để đưa người trả nhiều tiền nhất lên trên cùng (giảm dần)
    danh_sach_kh.sort(key=lambda x: x['tong_tien'], reverse=True)

    # 4. IN KẾT QUẢ
    for kh in danh_sach_kh:
        # Nối các thông tin bằng khoảng trắng
        print(f"{kh['ma']} {kh['ten']} {kh['phong']} {kh['so_ngay']} {kh['tong_tien']}")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()