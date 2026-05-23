import sys

def solve():
    # 1. Hút toàn bộ dữ liệu đầu vào thành một danh sách các từ/số
    input_data = sys.stdin.read().split()

    # Nếu file trống thì thoát luôn để tránh lỗi
    if not input_data:
        return

    t = int(input_data[0]) # Số lượng test case
    idx = 1 # Biến đánh dấu vị trí đang đọc dữ liệu

    # 2. Xử lý từng test case
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1

        # Tạo dãy số A
        a = []
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1

        so_luong_chen = 0

        # 3. Duyệt qua từng CẶP SỐ ĐỨNG CẠNH NHAU trong mảng
        # Chạy từ 0 đến n-2 để khi gọi a[i+1] không bị văng lỗi vượt quá giới hạn
        for i in range(n - 1):
            so_nho = min(a[i], a[i+1])
            so_lon = max(a[i], a[i+1])

            # 4. BẮC CẦU
            # Trong khi "bậc thang" còn quá dốc (số lớn > 2 lần số nhỏ)
            while so_lon > 2 * so_nho:
                # Chèn thêm một bậc thang cao gấp đôi số nhỏ hiện tại
                so_nho = so_nho * 2

                # Ghi sổ: Đã chèn thêm 1 số
                so_luong_chen += 1

        # In ra số lượng phép chèn ít nhất cho test case hiện tại
        print(so_luong_chen)

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
