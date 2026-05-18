import sys


def solve():
    # Đọc dữ liệu đầu vào chống trôi dòng
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    for _ in range(T):
        N = int(input_data[idx])
        idx += 1

        # Biến chứa tất cả các đáp án (ví dụ: ["(4)", "(3 1)", "(2 2)"])
        danh_sach_ket_qua = []

        # --- HÀM QUAY LUI (BACKTRACKING) ---
        def quay_lui(so_con_lai, max_duoc_chon, gio_hien_tai):
            # Điều kiện dừng: Nếu không còn kẹo nào để chia -> Đã chia thành công!
            if so_con_lai == 0:
                # Ép các số thành chuỗi, nối bằng khoảng trắng và bọc dấu ngoặc ()
                chuoi_dap_an = "(" + " ".join(map(str, gio_hien_tai)) + ")"
                danh_sach_ket_qua.append(chuoi_dap_an)
                return  # Quay lại bước trước đó

            # Tìm giới hạn cho vòng lặp:
            # Không được lấy nhiều hơn số kẹo còn lại,
            # VÀ không được lấy nhiều hơn số vừa lấy trước đó (để tránh lặp và in đúng thứ tự)
            gioi_han = min(so_con_lai, max_duoc_chon)

            # Thử lấy kẹo từ số lượng lớn nhất giảm dần về 1
            for so_keo_thu_lay in range(gioi_han, 0, -1):
                # BƯỚC 1: THỬ
                # Bỏ số kẹo này vào giỏ
                gio_hien_tai.append(so_keo_thu_lay)

                # BƯỚC 2: ĐI TIẾP
                # Gọi đệ quy để máy tính tiếp tục chia phần kẹo dư
                quay_lui(so_con_lai - so_keo_thu_lay, so_keo_thu_lay, gio_hien_tai)

                # BƯỚC 3: QUAY LUI (BACKTRACK)
                # Máy đã thử xong kịch bản trên. Giờ ta phải nhấc viên kẹo vừa bỏ vào ra khỏi giỏ
                # để vòng lặp for có thể tiếp tục thử con số bé hơn tiếp theo.
                gio_hien_tai.pop()

        # --- BẮT ĐẦU CHẠY HÀM ---
        # Bắt đầu với N viên kẹo, được phép chọn tối đa N viên, giỏ ban đầu trống rỗng []
        quay_lui(N, N, [])

        # In kết quả theo đúng chuẩn đề bài
        print(len(danh_sach_ket_qua))  # Dòng 1: Số lượng cách chia
        print(" ".join(danh_sach_ket_qua))  # Dòng 2: Danh sách cách chia cách nhau khoảng trắng


if __name__ == '__main__':
    solve()