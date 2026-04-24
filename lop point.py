import math
from decimal import Decimal # Bắt buộc phải import thư viện này theo yêu cầu của hệ thống

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # Tính khoảng cách bằng công thức sqrt((x1-x2)^2 + (y1-y2)^2)
        dist = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

        # TRỌNG TÂM Ở ĐÂY: Vì hệ thống gọi print(p1.distance(p2))
        # nên hàm này bắt buộc phải trả về CHUỖI đã được làm tròn 4 số thập phân.
        return f"{dist:.4f}"

# --- ĐOẠN CODE DƯỚI ĐÂY LÀ BẮT BUỘC GIỮ NGUYÊN THEO ĐỀ BÀI ---
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
