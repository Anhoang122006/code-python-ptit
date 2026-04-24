import math
import sys

# Thầy gán lại input để code của em vẫn dùng input() nhưng chạy nhanh hơn
input = sys.stdin.readline

def solve():
    # Bước 1: Nhập số lượng trò chơi T
    line_t = input().strip()
    if not line_t:
        return
    t = int(line_t)

    for _ in range(t):
        # Bước 2: Nhập dữ liệu cho mỗi trò chơi
        line_n = input().strip()
        if not line_n:
            continue
        n = int(line_n)

        # Nhập mảng a (độ dài bước nhảy) và c (chi phí)
        a = list(map(int, input().split()))
        c = list(map(int, input().split()))

        # dp[gcd_hien_tai] = chi_phi_nho_nhat_tuong_ung
        dp = {}

        # Bước 3: Duyệt qua từng thẻ để cập nhật trạng thái GCD
        for i in range(n):
            curr_a = a[i]
            curr_c = c[i]

            # Tạo một từ điển tạm để chứa các trạng thái mới sinh ra ở lượt này
            new_states = {}

            # 1. Xét trường hợp chỉ dùng đúng thẻ hiện tại
            new_states[curr_a] = curr_c

            # 2. Kết hợp thẻ hiện tại với tất cả các GCD đã tìm được trước đó
            for g, cost in dp.items():
                moi_gcd = math.gcd(g, curr_a)
                moi_cost = cost + curr_c

                # Nếu GCD này mới hoặc tìm được cách rẻ hơn thì cập nhật vào new_states
                if moi_gcd not in new_states or moi_cost < new_states[moi_gcd]:
                    new_states[moi_gcd] = moi_cost

            # Cập nhật ngược lại vào dp chính
            for g, cost in new_states.items():
                if g not in dp or cost < dp[g]:
                    dp[g] = cost

        # Bước 4: In kết quả cho bộ test hiện tại
        if 1 in dp:
            print(dp[1])
        else:
            print("-1")

if __name__ == "__main__":
    solve()
