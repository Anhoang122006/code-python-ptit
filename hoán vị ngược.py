import sys


# Hàm tính giai thừa để biết trước số lượng hoán vị (N!)
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    for _ in range(T):
        N = int(input_data[idx])
        idx += 1

        results = []  # Nơi chứa các hoán vị tìm được
        current_perm = []  # Hàng số đang xếp dở
        used = [False] * (N + 1)  # Sổ ghi chép: số nào đã dùng rồi?

        # --- HÀM QUAY LUI ---
        def backtrack():
            # Nếu hàng đã đủ N người
            if len(current_perm) == N:
                # Nối các số lại thành một chuỗi (vd: [3, 2, 1] -> "321")
                results.append("".join(map(str, current_perm)))
                return

            # Duyệt từ N về 1 để ưu tiên số lớn đứng trước (thứ tự ngược)
            for i in range(N, 0, -1):
                if not used[i]:
                    # 1. THỬ: Đặt số i vào hàng
                    used[i] = True
                    current_perm.append(i)

                    # 2. ĐI TIẾP: Xếp các vị trí còn lại
                    backtrack()

                    # 3. QUAY LUI: Nhấc số i ra để thử số khác bé hơn
                    current_perm.pop()
                    used[i] = False

        # Chạy máy
        backtrack()

        # In kết quả theo đúng chuẩn đề bài
        print(len(results))  # Dòng 1: Tổng số cách (N!)
        print(" ".join(results))  # Dòng 2: Các hoán vị cách nhau khoảng trắng


if __name__ == '__main__':
    solve()