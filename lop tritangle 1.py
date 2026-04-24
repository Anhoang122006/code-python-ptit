import math
import sys

# 1. TÁI SỬ DỤNG LỚP POINT TỪ BÀI 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # Tính khoảng cách giữa điểm hiện tại và điểm "other"
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# 2. XÂY DỰNG LỚP TRIANGLE (TAM GIÁC)
class Triangle:
    def __init__(self, p1, p2, p3):
        # Tam giác được cấu tạo từ 3 điểm
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_chu_vi(self):
        # Tính độ dài 3 cạnh bằng cách gọi hàm distance của Lớp Point
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)

        # Kiểm tra điều kiện hình thành tam giác (Bất đẳng thức tam giác)
        if a + b > c and a + c > b and b + c > a:
            chu_vi = a + b + c
            # Trả về chu vi làm tròn 3 chữ số thập phân
            return f"{chu_vi:.3f}"
        else:
            return "INVALID"

def solve():
    # Đọc TOÀN BỘ dữ liệu vào một mảng duy nhất để chống lại mọi test case xuống dòng lộn xộn
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0]) # Số lượng test case
    idx = 1          # Con trỏ duyệt mảng data

    for _ in range(t):
        # Lấy 6 số tiếp theo để tạo 3 điểm
        p1 = Point(float(data[idx]), float(data[idx+1]))
        p2 = Point(float(data[idx+2]), float(data[idx+3]))
        p3 = Point(float(data[idx+4]), float(data[idx+5]))
        idx += 6

        # Đưa 3 điểm vào "khuôn" để đúc ra Tam giác
        tri = Triangle(p1, p2, p3)

        # In kết quả
        print(tri.get_chu_vi())

if __name__ == '__main__':
    solve()
