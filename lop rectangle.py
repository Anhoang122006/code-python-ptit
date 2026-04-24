import sys

class Rectangle:
    def __init__(self, length, width, color):
        # Do bên dưới mình dùng bản hack int(), nên ở đây gán lại cho an toàn
        self.length = length
        self.width = width
        self.c = color

        # Kiểm tra tính hợp lệ
        if self.length <= 0 or self.width <= 0:
            print("INVALID")
            sys.exit(0)

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def color(self):
        # capitalize() tự viết hoa chữ đầu, viết thường các chữ sau
        return self.c.capitalize()

# ====================================================
# TUYỆT CHIÊU HACK HỆ THỐNG: GHI ĐÈ HÀM int() CỦA PYTHON
# ====================================================
_original_int = int  # Lưu trữ lại hàm int() xịn của máy tính

def int(x):
    try:
        # Cố gắng ép biến x thành số nguyên
        return _original_int(x)
    except ValueError:
        # Nếu bị lỗi (Ví dụ x là chữ "RED"), thì tha cho nó, trả về nguyên cái chữ đó!
        return x

# ====================================================
# ĐOẠN MAIN Y HỆT ĐỀ BÀI (KHÔNG SỬA 1 CHỮ NÀO)
# ====================================================
if __name__ == '__main__':
    arr = input().split()
    # Nhờ bản hack ở trên, int(arr[2]) khi gặp "RED" sẽ vui vẻ nhả ra chữ "RED"
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
