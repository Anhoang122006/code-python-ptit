# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Nhập dữ liệu
n = int(input())
A = list(map(int, input().split()))

# Tạo dãy B (loại trùng, giữ thứ tự)
B = []
for x in A:
    if x not in B:
        B.append(x)

m = len(B)

# Duyệt tìm vị trí i
found = False

for i in range(m):
    # Tính tổng bên trái
    left_sum = sum(B[:i+1])

    # Tính tổng bên phải
    right_sum = sum(B[i+1:])

    # Kiểm tra nguyên tố
    if is_prime(left_sum) and is_prime(right_sum):
        print(i)
        found = True
        break

# Nếu không tìm thấy
if not found:
    print("NOT FOUND")
