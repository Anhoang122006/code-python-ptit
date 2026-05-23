def solve():
    try:
        # Mở file để đọc dữ liệu
        with open('DATA.in', 'r') as file:
            # .read().split() tự động hút toàn bộ văn bản và chia thành các từ
            danh_sach_tu = file.read().split()
    except FileNotFoundError:
        # Đề phòng trường hợp file chưa tồn tại
        return

    # Mảng chứa các từ thỏa mãn điều kiện (không phải là số nguyên 32-bit)
    ket_qua = []

    # Duyệt qua từng từ trong file
    for tu in danh_sach_tu:
        try:
            # THỬ ÉP KIỂU
            # Nếu 'tu' là "123A", lệnh này sẽ gây ra lỗi và nhảy thẳng xuống nhánh except
            gia_tri = int(tu)

            # Nếu ép kiểu thành công, kiểm tra xem nó có tràn viền 32-bit không
            # Nếu bé hơn -2147483648 hoặc lớn hơn 2147483647 thì giữ lại
            if gia_tri < -2147483648 or gia_tri > 2147483647:
                ket_qua.append(tu)

        except ValueError:
            # Nhánh này bắt các từ không thể biến thành số (chứa chữ cái, ký tự đặc biệt...)
            ket_qua.append(tu)

    # Sắp xếp mảng kết quả theo thứ tự từ điển (A-Z)
    ket_qua.sort()

    # In ra tất cả trên một dòng, cách nhau bởi khoảng trắng
    print(" ".join(ket_qua))

# Kích hoạt chương trình
if __name__ == '__main__':
    solve()
