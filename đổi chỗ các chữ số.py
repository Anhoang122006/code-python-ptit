def solve():
    # Đọc số lượng test case
    t_str = input().strip()
    if not t_str:
        return
    T = int(t_str)

    for _ in range(T):
        # Đọc chuỗi số của mỗi test case
        s = input().strip()

        # 1. TÌM ĐIỂM GÃY (Từ phải qua trái)
        i = len(s) - 2
        while i >= 0 and s[i] <= s[i+1]:
            i -= 1

        # Nếu đi hết chuỗi mà không thấy điểm gãy -> Dãy tăng dần (VD: 123)
        if i == -1:
            print("-1")
            continue

        # 2. TÌM NGƯỜI THAY THẾ (Bên phải điểm gãy)
        max_val = -1
        best_j = -1

        for j in range(i + 1, len(s)):
            # Tiêu chí 1: Nhỏ hơn s[i]
            if s[j] < s[i]:
                # Tiêu chí 2 & 3: Lớn nhất có thể và ưu tiên đứng bên trái
                # Dùng dấu '>' sẽ tự động bỏ qua các số bằng nhau nằm ở xa hơn
                if int(s[j]) > max_val:
                    max_val = int(s[j])
                    best_j = j

        # 3. TRÁO ĐỔI VỊ TRÍ
        # Chuyển chuỗi thành mảng (list) để có thể thay đổi từng phần tử
        arr = list(s)
        arr[i], arr[best_j] = arr[best_j], arr[i]

        # 4. KIỂM TRA LUẬT LỆ (Không có số 0 ở đầu)
        if arr[0] == '0':
            print("-1")
        else:
            # Ghép mảng lại thành chuỗi và in ra
            print("".join(arr))

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
