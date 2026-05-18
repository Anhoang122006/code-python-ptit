import sys


def solve():
    # 1. Đọc dữ liệu đầu vào siêu tốc
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    a = []
    for i in range(1, N + 1):
        a.append(int(input_data[i]))

    # Tìm giới hạn lớn nhất của thương số K
    # K không thể vượt quá giá trị nhỏ nhất trong mảng A
    min_A = min(a)

    # Biến lưu trữ đáp án (tổng nhỏ nhất của mảng B)
    # Khởi tạo bằng vô cùng lớn
    ans = float('inf')

    # 2. Thử từng trường hợp của thương số K (từ 1 đến min_A)
    for k in range(1, min_A + 1):
        current_sum_B = 0
        is_valid_K = True  # Cờ đánh dấu K hợp lệ

        # 3. Với mỗi K, kiểm tra xem toàn bộ mảng A có tạo ra mảng B hợp lệ không
        for num in a:
            # Công thức Toán học giới hạn của B
            max_b = num // k
            min_b = num // (k + 1) + 1

            # Nếu min > max, chứng tỏ không có số nguyên nào thỏa mãn phép chia này
            if min_b > max_b:
                is_valid_K = False
                break  # Vứt bỏ K này, không cần kiểm tra các số A còn lại nữa

            # Nếu hợp lệ, ta luôn lấy min_b để đảm bảo tổng B là nhỏ nhất
            current_sum_B += min_b

        # 4. Nếu K này vượt qua mọi bài kiểm tra, so sánh tổng B với kỷ lục hiện tại
        if is_valid_K:
            ans = min(ans, current_sum_B)

    # In ra đáp án cuối cùng
    print(ans)


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()