import sys
from math import gcd

def solve():
    # Sử dụng sys.stdin.read().split() để đọc dữ liệu siêu nhanh cho hệ CLC
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    t = int(next(it))

    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        min_len = float('inf')
        # current_gcds lưu {giá_trị_gcd: độ_dài_ngắn_nhất}
        current_gcds = {}

        for x in a:
            new_gcds = {x: 1} # Bản thân phần tử hiện tại là 1 dãy con độ dài 1

            # Kết hợp x với tất cả các GCD kết thúc ở phần tử ngay trước đó
            for g, length in current_gcds.items():
                new_g = gcd(g, x)
                # Nếu chưa có new_g hoặc tìm được dãy ngắn hơn thì cập nhật
                if new_g not in new_gcds or length + 1 < new_gcds[new_g]:
                    new_gcds[new_g] = length + 1

            # Kiểm tra xem có tạo được GCD bằng K không
            if k in new_gcds:
                min_len = min(min_len, new_gcds[k])

            current_gcds = new_gcds

        if min_len == float('inf'):
            print(-1)
        else:
            print(min_len)

if __name__ == "__main__":
    solve()
