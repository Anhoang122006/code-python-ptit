import sys

def solve():
    # Đọc dữ liệu và loại bỏ khoảng trắng thừa
    data = sys.stdin.read().split()
    if not data:
        return

    s = data[0]

    # Bước 1: Xử lý số âm và đếm bước đầu tiên
    # Nếu là số âm, ví dụ "-123", bước đầu tiên là tính tổng |-1| + 2 + 3 = 6
    # Hoặc đơn giản là lấy giá trị tuyệt đối của các chữ số.

    count = 0

    # Trường hợp số có 1 chữ số ngay từ đầu
    if len(s) == 1 or (s.startswith('-') and len(s) == 2):
        print(1)
        return

    # Nếu là số âm, ta xử lý riêng lần đầu để chuyển về số dương
    if s.startswith('-'):
        # Lấy giá trị tuyệt đối của chữ số đầu tiên sau dấu trừ và các chữ số còn lại
        # Ví dụ: -19 -> |-1| + 9 = 10
        first_digit = int(s[1])
        remaining_digits_sum = sum(int(d) for d in s[2:])
        s = str(first_digit + remaining_digits_sum)
        count += 1

    # Tiếp tục vòng lặp cho đến khi còn 1 chữ số
    while len(s) > 1:
        tong = sum(int(d) for d in s)
        s = str(tong)
        count += 1

    print(count)

if __name__ == "__main__":
    solve()
