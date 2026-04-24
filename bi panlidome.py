# Hàm chuyển số n sang hệ cơ số k
def convert_to_base(n, k):
    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJ" # Bảng ký tự cho hệ cơ số lên đến 20
    result = ""

    temp_n = n
    while temp_n > 0:
        du = temp_n % k
        result = digits[du] + result
        temp_n //= k

    return result

# Hàm kiểm tra chuỗi đối xứng
def is_palindrome(s):
    # So sánh chuỗi s với chuỗi đảo ngược của nó s[::-1]
    return s == s[::-1]

def solve():
    while True:
        line = input()

        if line == "-1":
            break

        data = line.split()

        x = int(data[0])
        a = int(data[1])
        b = int(data[2])


        s_a = convert_to_base(x, a)
        check_a = is_palindrome(s_a)


        s_b = convert_to_base(x, b)
        check_b = is_palindrome(s_b)

        if check_a and check_b:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
