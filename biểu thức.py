import sys


def solve():
    # 1. Đọc dữ liệu đầu vào.
    # Lưu ý: Dùng splitlines() thay vì split() vì biểu thức có chứa khoảng trắng,
    # nếu dùng split() nó sẽ cắt nát biểu thức của cậu ra.
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    T = int(input_data[0].strip())

    # 2. Xử lý từng bộ test
    for i in range(1, T + 1):
        if i >= len(input_data):
            break

        bieu_thuc = input_data[i]

        stack = []  # Đây chính là "chồng đĩa"
        ket_qua = []  # Cuốn sổ ghi kết quả
        so_thu_tu = 1  # Cuộn tem số thứ tự bắt đầu từ 1

        # 3. Duyệt qua từng ký tự của biểu thức
        for ky_tu in bieu_thuc:
            if ky_tu == '(':
                # Gặp mở ngoặc: Đẩy số thứ tự vào chồng đĩa, ghi sổ, rồi tăng số lên
                stack.append(so_thu_tu)
                ket_qua.append(str(so_thu_tu))
                so_thu_tu += 1

            elif ky_tu == ')':
                # Gặp đóng ngoặc: Rút chiếc đĩa trên cùng ra và ghi sổ
                # Vì đề bài cam kết biểu thức luôn đúng, ta không sợ stack bị rỗng
                id_ngoac = stack.pop()
                ket_qua.append(str(id_ngoac))

        # 4. In kết quả của dòng hiện tại, nối nhau bằng khoảng trắng
        print(" ".join(ket_qua))


# Kích hoạt chương trình
if __name__ == '__main__':
    solve()