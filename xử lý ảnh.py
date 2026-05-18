import sys


def solve():
    # 1. Đọc dữ liệu siêu tốc
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []

    for _ in range(T):
        N = int(input_data[idx])  # Số hàng
        M = int(input_data[idx + 1])  # Số cột
        L = int(input_data[idx + 2])  # Kích thước kính lúp (Luôn là số lẻ)
        idx += 3

        # Tạo ma trận gốc A (Thêm 1 hàng 0 và 1 cột 0 ở rìa để dễ tính toán)
        a = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                a[i][j] = int(input_data[idx])
                idx += 1

        # 2. LẬP SỔ KẾ TOÁN (Mảng cộng dồn 2 chiều)
        pref = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                # Tổng hình chữ nhật từ góc (1,1) đến (i,j)
                pref[i][j] = (a[i][j] +
                              pref[i - 1][j] +
                              pref[i][j - 1] -
                              pref[i - 1][j - 1])

        # 3. TRƯỢT KÍNH LÚP QUA ẢNH
        k = L // 2  # Bán kính của kính lúp (Ví dụ L=5 -> k=2)
        area = L * L  # Diện tích kính lúp (Dùng để chia trung bình)

        # Tâm (i, j) của kính lúp không được chạm ra ngoài rìa ảnh
        # Hàng i chỉ chạy từ (k+1) đến (N-k)
        for i in range(k + 1, N - k + 1):
            row_result = []

            # Cột j chỉ chạy từ (k+1) đến (M-k)
            for j in range(k + 1, M - k + 1):
                # Xác định 2 góc của kính lúp
                r1, c1 = i - k, j - k  # Góc trên cùng bên trái
                r2, c2 = i + k, j + k  # Góc dưới cùng bên phải

                # Áp dụng công thức tính tổng O(1) thần thánh
                total_sum = (pref[r2][c2]
                             - pref[r1 - 1][c2]
                             - pref[r2][c1 - 1]
                             + pref[r1 - 1][c1 - 1])

                # Tính trung bình và làm tròn xuống (Dùng phép chia nguyên //)
                avg = total_sum // area

                # Lưu vào kết quả của hàng hiện tại
                row_result.append(str(avg))

            # Đẩy hàng hiện tại vào danh sách in ra màn hình
            out.append(" ".join(row_result))

    # In toàn bộ kết quả cực nhanh
    print('\n'.join(out))


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()