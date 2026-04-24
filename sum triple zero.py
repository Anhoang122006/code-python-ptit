import sys

# Dùng readline để tăng tốc độ nhập liệu
input = sys.stdin.read

def solve():
    # Đọc toàn bộ dữ liệu một lần
    data = input().split()
    if not data:
        return

    idx = 0
    t = int(data[idx])
    idx += 1

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        # Lấy n phần tử tiếp theo và sắp xếp
        a = sorted([int(x) for x in data[idx : idx + n]])
        idx += n

        s = 0
        # Vòng lặp i chạy từ 0 đến n-3
        for i in range(n - 2):
            # Tối ưu: Nếu a[i] > 0 thì không bao giờ tổng 3 số dương bằng 0 được (vì mảng đã sort)
            if a[i] > 0:
                break

            # Tối ưu: Bỏ qua số trùng ở vị trí i để tránh đếm lặp và tốn công
            if i > 0 and a[i] == a[i-1]:
                continue

            l = i + 1
            r = n - 1
            target = -a[i]

            while l < r:
                current_sum = a[l] + a[r]
                if current_sum == target:
                    s += 1
                    l += 1
                    # Em có thể thêm logic bỏ qua trùng ở đây nếu bài toán yêu cầu
                    # đếm các bộ chỉ số khác nhau thay vì bộ giá trị khác nhau.
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1
        print(s)

if __name__ == "__main__":
    solve()
