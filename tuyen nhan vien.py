import sys


def chuan_hoa_diem(diem):
  while diem > 10:
    diem /= 10
  return diem


class ThiSinh():
  def __init__(self,stt,ten,diem_lt,diem_th):
    self.ma_ts=f"TS{stt:02d}"# Tạo mã: stt=1 -> TS01, stt=12 -> TS12. (:02d giúp chèn số 0 ở trước)
    self.ten=ten
    self.diem_lt=chuan_hoa_diem(diem_lt)
    self.diem_th=chuan_hoa_diem(diem_th)
    self.diem_tb=(self.diem_lt+self.diem_th)/2
  def lay_xep_loai(self):
    if self.diem_tb<5:
      return "TRUOT"
    elif self.diem_tb<8:
      return "CAN NHAC"
    elif self.diem_tb<=9.5:
      return "DAT"
    else:
      return "XUAT SAC"
  def display(self):
    xep_loai=self.lay_xep_loai()
    print(f"{self.ma_ts} {self.ten} {self.diem_tb:.2f} {xep_loai}")

def solve():
  n=int(input())
  danh_sach=[]
  for i in range(1,n+1):
      ten=input()
      diem_lt=float(input())
      diem_th=float(input())
      ts = ThiSinh(i, ten, diem_lt, diem_th)
      danh_sach.append(ts)
  danh_sach.sort(key=lambda x: x.diem_tb, reverse=True)
  for ts in danh_sach:
        ts.display()


solve()
