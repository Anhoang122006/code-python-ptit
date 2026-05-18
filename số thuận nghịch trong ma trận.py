import sys


# --- HÀM PHỤ TRỢ: KIỂM TRA SỐ THUẬN NGHỊCH ---
def check_thuan_nghich(chuoi_so):
    # Điều kiện 1: Phải có từ 2 chữ số trở lên
    if len(chuoi_so) < 2:
        return False

    # Điều kiện 2: Đọc xuôi và đọc ngược (soi gương) phải giống hệt nhau
    # Kỹ thuật [::-1] trong Python giúp lật ngược chuỗi ngay lập tức
    if chuoi_so == chuoi_so[::-1]:
        return True

    return False


# --- HÀM CHÍNH ---
def solve():
    # 1. Đọc toàn bộ dữ liệu đầu vào (Bỏ qua khoảng trắng, xuống dòng lộn xộn)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])  # Số hàng
    M = int(input_data[1])  # Số cột

    # Đưa dữ liệu vào ma trận (Mảng 2 chiều)
    idx = 2
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            # Lưu dữ liệu dưới dạng "Chuỗi" (String) để lát nữa dễ lật ngược soi gương
            row.append(input_data[idx])
            idx += 1
        matrix.append(row)

    # 2. VÒNG QUÉT 1: Tìm "tên trùm" (Số thuận nghịch lớn nhất)
    # Khởi tạo giá trị lớn nhất là -1 (vì các số trong ma trận đều >= 0)
    max_val = -1

    for i in range(N):
        for j in range(M):
            chuoi_hien_tai = matrix[i][j]

            # Nếu nó là số thuận nghịch
            if check_thuan_nghich(chuoi_hien_tai):
                so_hien_tai = int(chuoi_hien_tai)  # Ép kiểu về số nguyên để so sánh lớn bé
                if so_hien_tai > max_val:
                    max_val = so_hien_tai

    # 3. VÒNG QUÉT 2 & KẾT LUẬN
    if max_val == -1:
        # Nếu quét xong mà max_val vẫn là -1, nghĩa là không tìm thấy số nào
        print("NOT FOUND")
    else:
        # Nếu tìm thấy, in giá trị lớn nhất ra trước
        print(max_val)

        # Quét lại ma trận lần nữa để in ra tất cả các tọa độ của nó
        for i in range(N):
            for j in range(M):
                if int(matrix[i][j]) == max_val:
                    # Đề bài yêu cầu in chỉ số bắt đầu từ 0
                    print(f"Vi tri [{i}][{j}]")


if __name__ == '__main__':
    solve()