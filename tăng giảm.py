import sys


def solve():
    # 1. Hút dữ liệu siêu tốc
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []

    for _ in range(T):
        N = int(input_data[idx])
        idx += 1

        # 2. Tách dữ liệu thành 2 mảng Chiều cao (A) và Cân nặng (B)
        A = []
        B = []
        for _ in range(N):
            A.append(float(input_data[idx]))
            B.append(float(input_data[idx + 1]))
            idx += 2

        # Nếu danh sách trống, kết quả là 0
        if N == 0:
            out.append("0")
            continue

        # 3. THUẬT TOÁN QUY HOẠCH ĐỘNG (DP)
        # Tạo mảng dp: dp[i] là độ dài hàng dài nhất kết thúc tại người i.
        # Ban đầu ai cũng tự thành một hàng dài 1.
        dp = [1] * N

        # Người i (người đứng chốt cuối hàng hiện tại)
        for i in range(1, N):
            # Nhìn lại những người j đứng trước i
            for j in range(i):
                # Kiểm tra xem i có đủ tiêu chuẩn đứng sau j không
                # Điều kiện: i phải cao hơn j (A[i] > A[j]) VÀ i phải nhẹ hơn j (B[i] < B[j])
                if A[i] > A[j] and B[i] < B[j]:
                    # Nếu thỏa mãn, thử nối đuôi i vào sau j.
                    # Lấy độ dài lớn nhất giữa (không nối) và (có nối)
                    dp[i] = max(dp[i], dp[j] + 1)

        # 4. KẾT LUẬN
        # Đội hình dài nhất có thể nằm ở bất kỳ người chốt đuôi nào,
        # nên ta đi tìm số lớn nhất trong toàn bộ cuốn sổ dp.
        out.append(str(max(dp)))

    # In ra toàn bộ kết quả cực nhanh
    print('\n'.join(out))


if __name__ == '__main__':
    solve()