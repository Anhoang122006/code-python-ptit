import math

class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu = tu_so
        self.mau = mau_so

    def toi_gian(self):
        # 1. Tìm Ước chung lớn nhất (UCLN) của tử và mẫu
        ucln = math.gcd(self.tu, self.mau)

        # 2. Chia cả tử và mẫu cho UCLN (Dùng phép chia nguyên // để không bị biến thành số thực)
        self.tu //= ucln
        self.mau //= ucln

    # Ma thuật của Python: Hàm quy định cách đối tượng được in ra màn hình
    def __str__(self):
        return f"{self.tu}/{self.mau}"

def solve():
    try:
        # Đọc dữ liệu đầu vào
        arr = input().split()

        # Ép kiểu sang số nguyên
        tu = int(arr[0])
        mau = int(arr[1])

        # Tạo đối tượng phân số
        ps = PhanSo(tu, mau)

        # Gọi phương thức rút gọn
        ps.toi_gian()

        # In phân số ra màn hình (Nó sẽ tự động gọi hàm __str__ ở trên)
        print(ps)

    except Exception as e:
        return

if __name__ == '__main__':
    solve()
