def check_so_dep(s):
    # 1. KIỂM TRA ĐIỀU KIỆN 1: Phải có đúng 2 chữ số khác nhau
    # set(s) giúp lọc ra các ký tự duy nhất
    # Ví dụ: set("121212") -> {'1', '2'} -> len là 2
    if len(set(s)) != 2:
        return False

    # 2. KIỂM TRA ĐIỀU KIỆN 2: Cách nhau 2 vị trí phải giống nhau
    # Ta bắt đầu chạy từ vị trí số 2 (ký tự thứ 3) trở đi
    for i in range(2, len(s)):
        # So sánh ký tự hiện tại với ký tự cách nó 2 bước về phía trước
        if s[i] != s[i - 2]:
            return False

    # Nếu vượt qua tất cả cửa ải trên
    return True


def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        if check_so_dep(s):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()