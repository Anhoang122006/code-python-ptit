# Hàm phụ trợ kiểm tra từ thuận nghịch
def check_thuan_nghich(tu):
    # Trả về True nếu từ đọc xuôi giống hệt đọc ngược
    return tu == tu[::-1]

def solve():
    try:
        # 1. Mở và đọc toàn bộ file
        with open('VANBAN.in', 'r') as file:
            # .read().split() tự động tách tất cả các từ, bỏ qua khoảng trắng/xuống dòng thừa
            danh_sach_tu = file.read().split()
    except FileNotFoundError:
        # Tránh lỗi sập chương trình nếu file không tồn tại
        return

    # 2. CHUẨN BỊ CÔNG CỤ
    danh_sach_thu_tu = []  # Tủ kính: Lưu các từ theo đúng thứ tự nhặt được
    tu_dien_dem = {}       # Cuốn sổ: Đếm số lần xuất hiện
    max_len = 0            # Biến lưu giữ kỷ lục độ dài lớn nhất

    # 3. QUÉT TỪNG TỪ TRONG FILE
    for tu in danh_sach_tu:
        if check_thuan_nghich(tu):
            # Cập nhật kỷ lục độ dài nếu tìm thấy từ to hơn
            if len(tu) > max_len:
                max_len = len(tu)

            # Nếu từ này mới xuất hiện lần đầu
            if tu not in tu_dien_dem:
                danh_sach_thu_tu.append(tu) # Đưa vào tủ kính trưng bày
                tu_dien_dem[tu] = 1         # Ghi vào sổ số 1
            else:
                # Nếu đã từng gặp, chỉ cần mở sổ ra cộng thêm 1
                tu_dien_dem[tu] += 1

    # 4. IN KẾT QUẢ
    # Đi dọc theo tủ kính (để đảm bảo đúng thứ tự xuất hiện ban đầu)
    for tu in danh_sach_thu_tu:
        # Chỉ in ra những từ đạt chuẩn "To nhất" (độ dài bằng max_len)
        if len(tu) == max_len:
            print(f"{tu} {tu_dien_dem[tu]}")

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
