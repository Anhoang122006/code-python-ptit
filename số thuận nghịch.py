def solve():
    try:
        # Lấy dữ liệu an toàn trên 1 dòng
        a, b, M = map(int, input().split())
    except Exception:
        return

    count = 0

    # Duyệt qua các số từ a đến b
    for x in range(a, b + 1):
        # Trường hợp ngoại lệ: 0 và 1 luôn là thuận nghịch trong mọi hệ cơ số
        if x == 0 or x == 1:
            count += 1
            continue

        # ----------------------------------------------------
        # PHỄU LỌC 1: Dùng hàm C-built-in của Python cho cơ số 2
        # Hàm bin(x) trả về chuỗi dạng "0b1011", nên ta cắt [2:] để lấy phần số "1011"
        # ----------------------------------------------------
        s_bin = bin(x)[2:]

        # Nếu soi gương không giống nhau -> Loại ngay lập tức!
        if s_bin != s_bin[::-1]:
            continue

        # ----------------------------------------------------
        # PHỄU LỌC 2: Dành cho ~4000 số tinh anh vượt qua Phễu 1
        # Thử nghiệm với các cơ số từ 3 đến M
        # ----------------------------------------------------
        is_valid = True
        for k in range(3, M + 1):
            # Mẹo Toán học: Chia hết cho k thì đuôi là 0 -> Chắc chắn không thuận nghịch
            if x % k == 0:
                is_valid = False
                break

            temp = x
            seq = []
            while temp > 0:
                seq.append(temp % k)
                temp //= k

            if seq != seq[::-1]:
                is_valid = False
                break

        # Nếu vượt qua tất cả các cơ số k
        if is_valid:
            count += 1

    # In ra kết quả duy nhất
    print(count)

if __name__ == '__main__':
    solve()
