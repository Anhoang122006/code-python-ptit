import sys
import bisect

# Gán lại để dùng input() nhưng vẫn đạt tốc độ cao
input = sys.stdin.readline

def solve():
    # Bước 1: Tạo trước danh sách số Hamming (Pre-compute)
    hamming = []
    limit = 10**18

    # Dùng 3 vòng lặp lồng nhau để tạo số 2^i * 3^j * 5^k
    p2 = 1
    while p2 <= limit:
        p3 = p2
        while p3 <= limit:
            p5 = p3
            while p5 <= limit:
                hamming.append(p5)
                # Nhân thêm 5 cho lượt kế tiếp
                p5 *= 5
            # Nhân thêm 3 cho lượt kế tiếp
            p3 *= 3
        # Nhân thêm 2 cho lượt kế tiếp
        p2 *= 2

    # Sắp xếp mảng để dùng Tìm kiếm nhị phân
    hamming.sort()

    # Bước 2: Nhập số lượng bộ test T
    line = input().strip()
    if not line:
        return
    t = int(line)

    # Bước 3: Xử lý từng bộ test
    for _ in range(t):
        n_str = input().strip()
        if not n_str:
            break
        n = int(n_str)

        # Dùng tìm kiếm nhị phân (bisect) để tìm vị trí của n
        idx = bisect.bisect_left(hamming, n)

        # Kiểm tra xem số tại vị trí đó có đúng bằng n không
        if idx < len(hamming) and hamming[idx] == n:
            # Thứ tự tính từ 1 nên ta lấy index + 1
            print(idx + 1)
        else:
            print("Not in sequence")

if __name__ == "__main__":
    solve()
