# Chúng ta không cần import sys vì bài này yêu cầu đọc từ file cụ thể

def solve():
    # 1. Tạo một cái hộp 'set' để tự động loại bỏ email trùng nhau
    danh_sach_du_uy_nhat = set()

    try:
        # 2. Mở file CONTACT.in để đọc ('r' là read)
        # Sử dụng 'with' là cách tốt nhất để đảm bảo file được đóng lại sau khi xong
        with open('CONTACT.in', 'r') as file:
            # Đọc từng dòng cho đến khi hết file
            for line in file:
                # Loại bỏ khoảng trắng/dấu xuống dòng ở 2 đầu
                email = line.strip()

                # Nếu dòng đó không trống
                if email:
                    # Chuyển về chữ thường (lowercase) và thêm vào set
                    # Cái hộp set sẽ tự lo việc loại bỏ nếu email đã tồn tại
                    danh_sach_du_uy_nhat.add(email.lower())

        # 3. Sắp xếp các email trong set theo thứ tự từ điển
        # Kết quả của hàm sorted() sẽ là một danh sách (list) đã được xếp từ A-Z
        ket_qua_da_sap_xep = sorted(list(danh_sach_du_uy_nhat))

        # 4. In kết quả ra màn hình
        for email in ket_qua_da_sap_xep:
            print(email)

    except FileNotFoundError:
        # Phòng trường hợp file CONTACT.in chưa được tạo
        pass


if __name__ == '__main__':
    solve()