def solve():
    # Lấy dữ liệu an toàn trên 1 dòng, loại bỏ khoảng trắng thừa
    s = input().strip()

    if not s:
        return

    # Xử lý ngoại lệ theo đúng ví dụ 3 của đề bài
    if len(s) == 1:
        print(1)
        return

    steps = 0

    # Lặp cho đến khi chiều dài chuỗi chỉ còn duy nhất 1 ký tự
    while len(s) > 1:
        tong = 0

        # Duyệt qua từng ký tự trong chuỗi
        for char in s:
            # Mô phỏng lại chính xác lỗi ép kiểu ký tự của C++
            # Ký tự '-' (ASCII 45) trừ đi '0' (ASCII 48) sẽ tự động biến thành -3
            tong += ord(char) - ord('0')

        # Biến tổng mới tính được thành chuỗi để kiểm tra chiều dài cho vòng lặp tiếp theo
        s = str(tong)

        # Ghi sổ 1 bước
        steps += 1

    # In ra tổng số bước
    print(steps)

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
