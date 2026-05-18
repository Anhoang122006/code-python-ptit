import sys


def solve():
    # 1. Đọc dữ liệu siêu tốc chống TLE
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    # Nạp dữ liệu vào mảng A
    A = []
    for i in range(1, N + 1):
        A.append(int(input_data[i]))

    # 2. TÌM CON SỐ "ĐỈNH" NHẤT
    # Dùng hàm max() của Python chạy cực nhanh
    max_val = max(A)

    # 3. ĐI TÌM DÃY CON DÀI NHẤT CHỈ CHỨA MAX
    ky_luc_dai_nhat = 0
    do_dai_hien_tai = 0

    for so in A:
        if so == max_val:
            # Nếu gặp đúng số lớn nhất, tăng chuỗi liên tiếp lên 1
            do_dai_hien_tai += 1

            # Nếu chuỗi này phá kỷ lục trước đó, cập nhật lại kỷ lục
            if do_dai_hien_tai > ky_luc_dai_nhat:
                ky_luc_dai_nhat = do_dai_hien_tai
        else:
            # Nếu gặp một số nhỏ hơn chen ngang, chuỗi liền kề bị đứt gãy.
            # Lập tức reset độ dài về 0 để đếm lại từ đầu khi gặp số MAX tiếp theo
            do_dai_hien_tai = 0

    # In ra kỷ lục cuối cùng
    print(ky_luc_dai_nhat)


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()