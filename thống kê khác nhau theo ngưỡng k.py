def solve():
    # 1. Đọc số dòng N và số K
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        k = int(line1[1])
    except EOFError:
        return

    # Tập hợp các dấu câu cần loại bỏ
    dau_cau = [',', '.', '?', '!', ':', ';', '(', ')', '-', '/']

    # Cuốn sổ tay ghi chép
    tu_dien = {}

    # 2. XỬ LÝ TỪNG DÒNG VĂN BẢN
    for _ in range(n):
        try:
            dong = input().lower()

            # Thay thế dấu câu bằng khoảng trắng
            for dau in dau_cau:
                dong = dong.replace(dau, ' ')

            cac_tu = dong.split()

            # Ghi vào sổ tay
            for tu in cac_tu:
                if tu in tu_dien:
                    tu_dien[tu] += 1
                else:
                    tu_dien[tu] = 1
        except EOFError:
            break

    # 3. LỌC VÀ SẮP XẾP
    # Tạo danh sách chỉ chứa những từ có số lần xuất hiện >= K
    danh_sach_loc = []
    for tu, so_lan in tu_dien.items():
        if so_lan >= k:
            danh_sach_loc.append((tu, so_lan))

    # Sắp xếp:
    # -x[1]: Tần suất giảm dần
    # x[0]: Từ vựng tăng dần (A-Z)
    danh_sach_loc.sort(key=lambda x: (-x[1], x[0]))

    # 4. IN KẾT QUẢ
    for tu, so_lan in danh_sach_loc:
        print(f"{tu} {so_lan}")

if __name__ == '__main__':
    solve()
