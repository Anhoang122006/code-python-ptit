import math
import sys

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toi_gian(self):
        # Rút gọn phân số bằng cách chia cho UCLN
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    # MA THUẬT Ở ĐÂY: Hàm __add__ giúp định nghĩa phép cộng (+) cho 2 phân số
    def __add__(self, other):
        # Quy đồng mẫu số và tính tử mới
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau

        # Tạo ra một phân số mới là kết quả của phép cộng
        ket_qua = PhanSo(tu_moi, mau_moi)

        # Tự động rút gọn phân số kết quả này trước khi trả về
        ket_qua.toi_gian()
        return ket_qua

    def __str__(self):
        # Định dạng in ra màn hình
        return f"{self.tu}/{self.mau}"

def solve():
    # Đọc tất cả các số có trên màn hình (đề phòng test case có dấu cách, xuống dòng lộn xộn)
    data = sys.stdin.read().split()
    if not data:
        return

    # Lấy 4 số nguyên để tạo 2 phân số p và q
    p = PhanSo(int(data[0]), int(data[1]))
    q = PhanSo(int(data[2]), int(data[3]))

    # Python sẽ tự động gọi hàm __add__ khi thấy dấu '+'
    tong = p + q

    # Python tự động gọi hàm __str__ khi thấy lệnh print
    print(tong)

if __name__ == '__main__':
    solve()
