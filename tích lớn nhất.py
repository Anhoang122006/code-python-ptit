def solve_max_product():
    # 1. Đọc dữ liệu đầu vào theo chuẩn thi đấu
    # Hàm input() đọc 1 dòng, int() ép kiểu sang số nguyên
    n = int(input())

    # Đọc dòng 2, tách các số bằng khoảng trắng và đưa vào mảng (List)
    a = list(map(int, input().split()))

    # 2. Sắp xếp mảng tăng dần
    a.sort()

    # 3. Tính toán các trường hợp

    # Xét tích 2 phần tử
    # So sánh: (2 số đầu - âm bé nhất) vs (2 số cuối - dương lớn nhất)
    max_2 = max(a[0] * a[1], a[-1] * a[-2])

    # Xét tích 3 phần tử
    # So sánh: (2 số đầu x số cuối) vs (3 số cuối)
    max_3 = max(a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3])

    # 4. In ra kết quả lớn nhất giữa 2 trường hợp
    print(max(max_2, max_3))


# Kích hoạt chương trình
if __name__ == '__main__':
    solve_max_product()