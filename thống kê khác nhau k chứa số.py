def solve():
    # 1. Đọc N
    try:
        n = int(input())
    except:
        return

    tu_dien = {}

    # 2. XỬ LÝ TỪNG DÒNG
    for _ in range(n):
        dong = input().lower()

        # BỘ LỌC ĐA TẦNG: Chuyển mọi thứ không phải chữ/số thành khoảng trắng
        dong_moi = ""
        for char in dong:
            if char.isalnum(): # Nếu là chữ cái hoặc số
                dong_moi += char
            else:
                dong_moi += " "

        # Tách từ
        cac_tu = dong_moi.split()

        # 3. KIỂM DUYỆT TỪ (Loại từ có chứa số)
        for tu in cac_tu:
            # Kiểm tra xem từ có chữ số không bằng cách kiểm tra any(c.isdigit())
            if any(char.isdigit() for char in tu):
                continue # Nếu có số -> Bỏ qua từ này

            # Nếu đạt chuẩn (toàn chữ cái), ghi vào sổ tay
            if tu in tu_dien:
                tu_dien[tu] += 1
            else:
                tu_dien[tu] = 1

    # 4. SẮP XẾP VÀ IN
    danh_sach = list(tu_dien.items())

    # Ưu tiên 1: Tần suất giảm dần (-x[1])
    # Ưu tiên 2: Từ vựng tăng dần (x[0])
    danh_sach.sort(key=lambda x: (-x[1], x[0]))

    for tu, so_lan in danh_sach:
        print(f"{tu} {so_lan}")

if __name__ == '__main__':
    solve()
