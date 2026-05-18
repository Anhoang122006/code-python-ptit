import sys


def solve():
    # 1. Hút toàn bộ dữ liệu đầu vào siêu tốc
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []

    for _ in range(T):
        N = int(input_data[idx])
        idx += 1

        # Tạo một mảng để chứa các đoạn thẳng
        doan_thang = []
        for _ in range(N):
            bat_dau = int(input_data[idx])
            ket_thuc = int(input_data[idx + 1])
            # Gói điểm đầu và điểm cuối thành 1 cặp (Tuple) rồi nhét vào mảng
            doan_thang.append((bat_dau, ket_thuc))
            idx += 2

        # 2. SẮP XẾP THEO ĐIỂM KẾT THÚC (Tuyệt chiêu Greedy)
        # Lệnh lambda x: x[1] mang ý nghĩa:
        # "Này Python, hãy sắp xếp mảng này dựa trên phần tử thứ 1 của mỗi cặp"
        # (Trong Python, đếm từ 0, nên x[0] là bắt đầu, x[1] là kết thúc)
        doan_thang.sort(key=lambda x: x[1])

        # 3. QUÉT VÀ NHẶT ĐOẠN THẲNG
        so_luong_chon = 0
        diem_ket_thuc_hien_tai = -1  # Khởi tạo bằng -1 vì tọa độ không âm

        for diem_dau, diem_cuoi in doan_thang:
            # Nếu điểm đầu của đoạn này >= điểm kết thúc của đoạn trước đó (không bị đè nhau)
            if diem_dau >= diem_ket_thuc_hien_tai:
                so_luong_chon += 1
                diem_ket_thuc_hien_tai = diem_cuoi  # Cập nhật lại mốc thời gian

        # Lưu kết quả của bộ test này
        out.append(str(so_luong_chon))

    # In ra toàn bộ đáp án
    print('\n'.join(out))


if __name__ == '__main__':
    solve()