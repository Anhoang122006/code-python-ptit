def solve():
    # 1. Đọc số lượng dòng N
    n_str = input().strip()
    if not n_str:
        return
    n = int(n_str)

    # Cuốn sổ tay ghi chép số lần xuất hiện
    tu_dien = {}

    # 2. XỬ LÝ TỪNG DÒNG
    for _ in range(n):
        dong = input().strip()

        # Biến tất cả thành chữ thường
        dong = dong.lower()

        # BỘ LỌC SIÊU CẤP: Thay vì xóa dấu câu, ta chỉ giữ lại chữ và số
        dong_moi = ""
        for char in dong:
            # Nếu ký tự nằm trong khoảng a-z hoặc 0-9 thì giữ lại
            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                dong_moi += char
            else:
                # Tất cả các ký tự rác khác (kể cả ngoặc kép, nháy đơn...) biến thành khoảng trắng
                dong_moi += " "

        # Tách từ dựa trên các khoảng trắng vừa tạo ra
        cac_tu = dong_moi.split()

        # 3. ĐẾM TỪ
        for tu in cac_tu:
            if tu in tu_dien:
                tu_dien[tu] += 1
            else:
                tu_dien[tu] = 1

    # 4. SẮP XẾP VÀ IN KẾT QUẢ
    danh_sach = list(tu_dien.items())

    # Xếp theo số lần giảm dần (-x[1]), nếu bằng nhau xếp theo từ vựng tăng dần (x[0])
    danh_sach.sort(key=lambda x: (-x[1], x[0]))

    for tu, so_lan in danh_sach:
        print(f"{tu} {so_lan}")

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
