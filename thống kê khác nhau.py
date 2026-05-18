import sys


def solve():
    # 1. Đọc toàn bộ văn bản đầu vào
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])

    # Tập hợp các dấu câu "đáng ghét" cần phải gọt bỏ
    dau_cau = [',', '.', '?', '!', ':', ';', '(', ')', '-', '/']

    # Khởi tạo cuốn sổ tay ghi chép số lần xuất hiện
    tu_dien = {}

    # 2. XỬ LÝ TỪNG DÒNG
    for i in range(1, n + 1):
        if i >= len(input_data):
            break
        dong = input_data[i]

        # Biến tất cả thành chữ thường
        dong = dong.lower()

        # Thay thế mọi dấu câu bằng khoảng trắng
        for dau in dau_cau:
            dong = dong.replace(dau, ' ')

        # Tách dòng thành các từ rời rạc
        # Hàm split() cực kỳ thông minh, nó tự động lọc bỏ các khoảng trắng thừa
        cac_tu = dong.split()

        # 3. ĐẾM TỪ (Ghi sổ)
        for tu in cac_tu:
            if tu in tu_dien:
                tu_dien[tu] += 1
            else:
                tu_dien[tu] = 1

    # 4. SẮP XẾP VÀ IN KẾT QUẢ
    # Chuyển sổ tay (Dictionary) thành một danh sách (List) các cặp để dễ sắp xếp
    # Ví dụ: [('lap', 5), ('trinh', 5), ('bai', 2)]
    danh_sach = list(tu_dien.items())

    # Tuyệt chiêu sắp xếp 2 điều kiện bằng Lambda:
    # x[1] là tần suất. Thêm dấu trừ (-) phía trước để Python xếp GIẢM DẦN.
    # x[0] là từ vựng. Cứ để nguyên để Python tự xếp TĂNG DẦN theo bảng chữ cái A-Z.
    danh_sach.sort(key=lambda x: (-x[1], x[0]))

    # In ra danh sách các từ sau khi đã xếp hạng
    for tu, so_lan in danh_sach:
        print(tu)


if __name__ == '__main__':
    solve()