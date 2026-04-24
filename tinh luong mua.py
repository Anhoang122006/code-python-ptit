class TramDo:
  def __init__(self,ma_tram,ten_tram):
    self.ma_tram=ma_tram
    self.ten_tram=ten_tram
    self.tong_luong_mua=0
    self.tong_thoi_gian=0
  def cap_nhat_du_lieu(self,bat_dau,ket_thuc,luong_mua):
    h1, m1 = map(int, bat_dau.split(':'))
    h2, m2 = map(int, ket_thuc.split(':'))
    thoi_gian_phut = (h2 * 60 + m2) - (h1 * 60 + m1)
    self.tong_luong_mua +=luong_mua
    self.tong_thoi_gian+= thoi_gian_phut
  def tinh_trung_binh(self):
    if self.tong_thoi_gian==0 : return 0.0
    return (self.tong_luong_mua / self.tong_thoi_gian) * 60
  def __str__(self):
    return f"{self.ma_tram} {self.ten_tram} {self.tinh_trung_binh():.2f}"
def solve():
  t=int(input())
  danh_sach_tram = []
  tra_cuu = {}
  stt_tra=1
  for _ in range(t):
    ten=input()
    bat_dau=input()
    ket_thuc=input()
    mua=float(input())
    if ten not in tra_cuu:
      ma=f"T{stt_tra:02d}"
      moi=TramDo(ma,ten)
      moi.cap_nhat_du_lieu(bat_dau,ket_thuc,mua)
      danh_sach_tram.append(moi)
      tra_cuu[ten]=moi
      stt_tra+=1
    else:
      tra_cuu[ten].cap_nhat_du_lieu(bat_dau,ket_thuc,mua)
  for tram in danh_sach_tram:
        print(tram)
if __name__ == "__main__":
    solve()


