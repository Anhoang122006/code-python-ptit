import sys


# --- HÀM PHỤ TRỢ: Tạo mã viết tắt ---
def tao_ma(chuoi):
    # Cắt chuỗi thành các từ (ví dụ: "Ha Noi" -> ["Ha", "Noi"])
    cac_tu = chuoi.split()
    ma = ""
    for tu in cac_tu:
        # Lấy chữ cái đầu tiên tu[0], viết hoa lên và cộng dồn vào mã
        ma += tu[0].upper()
    return ma


# --- HÀM CHÍNH ---
def solve():
    # 1. Đọc dữ liệu theo từng dòng chống trôi lệnh
    input_data = sys.stdin.read().splitlines()
    # Lọc bỏ các dòng trống vô tình gõ dư
    lines = [line.strip() for line in input_data if line.strip() != '']

    if not lines:
        return

    n = int(lines[0])
    idx = 1

    danh_sach_cua_ro = []

    # 2. XỬ LÝ TỪNG CUA-RƠ
    for _ in range(n):
        ten = lines[idx]
        don_vi = lines[idx + 1]
        thoi_diem_ve = lines[idx + 2]
        idx += 3

        # Tạo mã (Chữ cái đầu Đơn vị + Chữ cái đầu Tên)
        ma_vđv = tao_ma(don_vi) + tao_ma(ten)

        # Xử lý thời gian (Tách chuỗi "h:mm" thành Giờ và Phút)
        # map(int, ...) giúp biến chuỗi thành số ngay lập tức
        gio, phut = map(int, thoi_diem_ve.split(':'))

        # Tính thời gian chạy (bằng Giờ)
        thoi_gian_chay = (gio - 6) + (phut / 60)

        # Tính vận tốc (v = s / t)
        van_toc = 120 / thoi_gian_chay
        van_toc_lam_tron = round(van_toc)

        # Cất hồ sơ vào mảng
        danh_sach_cua_ro.append({
            'ma': ma_vđv,
            'ten': ten,
            'don_vi': don_vi,
            'van_toc': van_toc_lam_tron
        })

    # 3. SẮP XẾP DANH SÁCH
    # Dùng lambda để xếp theo vận tốc. Thêm dấu '-' để xếp GIẢM DẦN.
    danh_sach_cua_ro.sort(key=lambda x: -x['van_toc'])

    # 4. IN KẾT QUẢ
    for vdv in danh_sach_cua_ro:
        # Trong các bài PTIT, đơn vị "Km/h" thường được yêu cầu in kèm ở cuối dòng
        print(f"{vdv['ma']} {vdv['ten']} {vdv['don_vi']} {vdv['van_toc']} Km/h")


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()