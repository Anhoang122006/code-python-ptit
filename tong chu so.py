def solve_tong_chu_so():
    # Đọc số N dưới dạng chuỗi vì nó có thể dài tới 100.000 chữ số
    n_str = input().strip()

    # Trường hợp đặc biệt: Nếu số N chỉ có 1 chữ số ngay từ đầu
    if len(n_str) == 1:
        print(1) # Theo ví dụ: số 6 mất 1 bước để "chỉ còn duy nhất 1 chữ số"
        return

    buoc = 0
    while len(n_str) > 1:
        tong = 0
        # Duyệt từng ký tự chữ số trong chuỗi để tính tổng
        for chu_so in n_str:
            if chu_so == '-': # Bỏ qua dấu âm nếu có
                continue
            tong += int(chu_so)

        # Cập nhật n_str thành chuỗi của tổng mới để lặp lại
        n_str = str(tong)
        buoc += 1

    print(buoc)

if __name__=="__main__":
   solve_tong_chu_so()
