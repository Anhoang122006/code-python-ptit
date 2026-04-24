class CuonSach:
    def __init__(self, tua_de, tac_gia, so_trang):
        self.tua_de   = tua_de
        self.tac_gia  = tac_gia
        self.so_trang = so_trang

# Tạo 2 object
sach1 = CuonSach("Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 180)
sach2 = CuonSach("Số Đỏ", "Vũ Trọng Phụng", 320)

# In thông tin
print(sach1.tua_de)    # Dế Mèn Phiêu Lưu Ký
print(sach1.tac_gia)   # Tô Hoài
print(sach1.so_trang)  # 180

print(sach2.tua_de)    # Số Đỏ
print(sach2.tac_gia)   # Vũ Trọng Phụng
print(sach2.so_trang)  # 320
