import sys


def solve():
    # 1. Đọc dữ liệu siêu tốc (Trút toàn bộ file test vào bộ nhớ)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])  # Số lượng bài test
    idx = 1  # Biến đánh dấu vị trí đang đọc dữ liệu

    for _ in range(T):
        N = int(input_data[idx])
        K = int(input_data[idx + 1])
        idx += 2

        # Đưa các số vào mảng A (Băng chuyền)
        A = []
        for _ in range(N):
            A.append(int(input_data[idx]))
            idx += 1

        # Nếu K = 0 (Không cần chọn ai) thì tổng là 0
        if K == 0:
            print(0)
            continue

        M = 5 * K  # Tổng số người cần chọn

        # 2. Tạo mảng hệ số C
        # Dùng phép nhân mảng trong Python để tạo chuỗi lặp lại
        # Ví dụ K=2, C sẽ là: [1, -2, 3, -4, 5, 1, -2, 3, -4, 5]
        C = [1, -2, 3, -4, 5] * K

        # 3. LẬP BẢNG ĐIỂM (Quy hoạch động)
        # Tạo bảng gồm (N+1) hàng và (M+1) cột.
        # Ban đầu điền toàn bộ là "Âm vô cùng" (float('-inf'))
        # Vì lỡ như tổng ra số âm, nếu ta điền số 0 thì máy sẽ tưởng 0 là lớn nhất.
        dp = [[float('-inf')] * (M + 1) for _ in range(N + 1)]

        # Khởi tạo điểm xuất phát:
        # Cứ chưa chọn ai (Cột j = 0) thì điểm luôn bằng 0.
        for i in range(N + 1):
            dp[i][0] = 0

        # 4. BẮT ĐẦU CHẠY BĂNG CHUYỀN
        for i in range(1, N + 1):  # Lần lượt xét từng phần tử (từ 1 đến N)
            for j in range(1, M + 1):  # Thử mọi kịch bản chọn từ 1 đến M người

                # Kịch bản 1: BỎ QUA phần tử hiện tại (A[i-1])
                bo_qua = dp[i - 1][j]

                # Kịch bản 2: CHỌN phần tử hiện tại (A[i-1])
                chon = float('-inf')  # Đặt mặc định là cực thấp

                # Chỉ được CHỌN nếu trước đó (hàng i-1) đã đủ số lượng người (cột j-1)
                # Dấu != kiểm tra xem ô đó có hợp lệ không (khác âm vô cùng)
                if dp[i - 1][j - 1] != float('-inf'):
                    # Điểm cũ + (Giá trị phần tử * Hệ số tương ứng)
                    # Chú ý: C[j-1] vì mảng hệ số C đếm từ 0
                    chon = dp[i - 1][j - 1] + A[i - 1] * C[j - 1]

                # Ghi lại điểm cao nhất giữa 2 kịch bản vào bảng
                dp[i][j] = max(bo_qua, chon)

        # 5. KẾT LUẬN
        # Đáp án là ô nằm ở góc dưới cùng bên phải của bảng:
        # Tức là đã xét hết N người, và chọn đủ M người.
        print(dp[N][M])


# Cú pháp chuẩn để chạy chương trình Python
if __name__ == '__main__':
    solve()