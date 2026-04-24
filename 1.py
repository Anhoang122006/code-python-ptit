class Laptop:
    # 1. Hàm khởi tạo (Constructor) - Thiết lập "cấu hình" cho máy
    def __init__(self, thuong_hieu, model, cpu, ram, ssd):
        self.thuong_hieu = thuong_hieu  # Thuộc tính: Thương hiệu
        self.model = model              # Thuộc tính: Dòng máy
        self.cpu = cpu                  # Thuộc tính: Vi xử lý
        self.ram = ram                  # Thuộc tính: Bộ nhớ RAM
        self.ssd = ssd                  # Thuộc tính: Ổ cứng
        self.__is_on = False            # Tính đóng gói: Trạng thái nguồn (Private)

    # 2. Phương thức: Bật máy
    def bat_may(self):
        self.__is_on = True
        print(f"--- {self.model} đang khởi động... ---")

    # 3. Phương thức: Chạy code Python (Chuyên dụng cho dân IT)
    def chay_code_python(self, ten_bai_tap):
        if self.__is_on:
            print(f"[{self.model}] Đang thực thi bài tập: {ten_bai_tap}...")
            print(f"CPU {self.cpu} và {self.ram}GB RAM đang xử lý dữ liệu.")
            print("=> Kết quả: Accepted (AC)!")
        else:
            print("Lỗi: Máy chưa bật, không thể chạy code!")

# --- Chương trình chính ---
# Tạo đối tượng cụ thể từ cấu hình máy của Lân
my_laptop = Laptop("Asus", "Vivobook", "Core i5", 16, 512)

# Thực hiện các hành động
my_laptop.bat_may()
my_laptop.chay_code_python("Tìm số Hamming")
