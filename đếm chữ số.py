import sys


# --- HÀM CỐT LÕI: ĐẾM SỐ LƯỢNG CHỮ SỐ TỪ 1 ĐẾN N ---
def dem_chu_so(n):
    # Tạo một mảng 10 phần tử (từ 0 đến 9) để lưu kết quả, ban đầu toàn số 0
    ket_qua = [0] * 10

    if n <= 0:
        return ket_qua

    he_so = 1  # Đại diện cho hàng đang xét: 1 (đơn vị), 10 (chục), 100 (trăm)...

    # Vòng lặp duyệt qua từng cột (đơn vị, chục, trăm...)
    while he_so <= n:
        # Tách con số thành 3 phần như đã phân tích
        phan_dau = n // (he_so * 10)
        chu_so_hien_tai = (n // he_so) % 10
        phan_duoi = n % he_so

        # Đếm cho từng chữ số từ 0 đến 9
        for i in range(10):
            # Mặc định, mỗi chữ số sẽ xuất hiện (phan_dau * he_so) lần
            ket_qua[i] += phan_dau * he_so

            # Xử lý phần dư tùy thuộc vào chu_so_hien_tai
            if chu_so_hien_tai > i:
                ket_qua[i] += he_so
            elif chu_so_hien_tai == i:
                ket_qua[i] += phan_duoi + 1

        # TRƯỜNG HỢP ĐẶC BIỆT: Số 0
        # Số 0 không thể đứng ở đầu (không ai viết số 05, 005 cả)
        # Nên ta phải trừ đi lượng số 0 bị tính dư do công thức Toán học
        ket_qua[0] -= he_so

        # Chuyển sang hàng tiếp theo (từ đơn vị lên chục, chục lên trăm...)
        he_so *= 10

    return ket_qua


# --- HÀM CHÍNH ---
def solve():
    # Hút toàn bộ dữ liệu đầu vào chống trôi dòng
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []

    for _ in range(T):
        A = int(input_data[idx])
        B = int(input_data[idx + 1])
        idx += 2

        # Đề phòng trường hợp A lớn hơn B thì đổi chỗ
        if A > B:
            A, B = B, A

        # Áp dụng tư duy 1: Đếm(B) - Đếm(A - 1)
        dem_B = dem_chu_so(B)
        dem_A_tru_1 = dem_chu_so(A - 1)

        # Trừ từng phần tử của 2 mảng cho nhau
        ket_qua_cuoi = []
        for i in range(10):
            ket_qua_cuoi.append(dem_B[i] - dem_A_tru_1[i])

        # Nối kết quả thành chuỗi và đưa vào danh sách in
        out.append(" ".join(map(str, ket_qua_cuoi)))

    # In ra toàn bộ kết quả cực nhanh
    print('\n'.join(out))


if __name__ == '__main__':
    solve()