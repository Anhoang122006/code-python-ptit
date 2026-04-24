def solve():
   t=int(input())
   for _ in range(t):
      s=input()
      tong=0
      tich=1
      co_so_khac_khong = False
      for i in range(0,len(s),2):
         tong+=int(s[i])
      for i in range(1, len(s), 2):
            val = int(s[i])
            if val != 0:
                tich *= val
                co_so_khac_khong = True

            if not co_so_khac_khong:
                tich = 0
      print(tong, tich)

if __name__ == "__main__":
    solve()
