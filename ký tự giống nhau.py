import sys


def solve():
    # 1. Hút toàn bộ dữ liệu đầu vào (bỏ qua khoảng trắng và xuống dòng)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])  # Số lượng bộ test
    idx = 1

    # 2. Xử lý từng bộ test
    for _ in range(T):
        N = int(input_data[idx])
        X = int(input_data[idx + 1])
        Y = int(input_data[idx + 2])
        Z = int(input_data[idx + 3])
        idx += 4

        # Tạo "bảng ghi chép thành tích" dp
        # dp[i] sẽ lưu thời gian ít nhất để tạo ra i ký tự
        dp = [0] * (N + 1)

        # Khởi tạo giá trị đầu tiên: Để có 1 ký tự, bắt buộc phải dùng Insert (tốn X giây)
        dp[1] = X

        # 3. Vòng lặp điền bảng thành tích từ 2 đến N
        for i in range(2, N + 1):
            if i % 2 == 0:
                # Nếu i là SỐ CHẴN
                # So sánh: (Cách gõ thêm 1 chữ) vs (Cách nhân đôi từ một nửa)
                cach_1 = dp[i - 1] + X
                cach_2 = dp[i // 2] + Z
                dp[i] = min(cach_1, cach_2)
            else:
                # Nếu i là SỐ LẺ
                # So sánh: (Cách gõ thêm 1 chữ) vs (Cách nhân đôi lên vượt mức rồi xóa 1 chữ)
                cach_1 = dp[i - 1] + X
                # (i + 1) // 2 chính là số lượng ký tự cần có trước khi nhân đôi vượt mức
                cach_2 = dp[(i + 1) // 2] + Z + Y
                dp[i] = min(cach_1, cach_2)

        # 4. In ra kết quả ở ô thứ N (thời gian ít nhất để có N ký tự)
        print(dp[N])


if __name__ == '__main__':
    solve()