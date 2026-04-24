import sys

def check_prime(n):
    # Hàm kiểm tra số nguyên tố đơn giản
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    # Bước 1: Nhập dữ liệu N và X
    line = sys.stdin.readline().split()
    if not line: return
    n = int(line[0])
    x = int(line[1])

    # Bước 2: Tìm N số nguyên tố đầu tiên
    primes = []
    current_num = 2
    while len(primes) < n:
        if check_prime(current_num):
            primes.append(current_num)
        current_num += 1

    # Bước 3: Tạo dãy kết quả
    ans = [x]
    current_val = x
    for p in primes:
        current_val += p
        ans.append(current_val)

    # Bước 4: In kết quả trên một dòng cách nhau bởi dấu cách
    print(*(ans))

if __name__ == "__main__":
    solve()
