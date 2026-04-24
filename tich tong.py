def solve():
  t=int(input())
  for _ in range(t):
    s=input()
    tong=0
    tich=1
    for i in range(1,len(s),2):
      tong+=int(s[i])
    for i in range(0,len(s),2):
      if int(s[i])!=0:
        tich*=int(s[i])
    print(tich, tong)

if __name__ == "__main__":
    solve()
