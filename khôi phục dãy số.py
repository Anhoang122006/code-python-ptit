def solve():
  n=int(input())
  mb=[]
  for i in range(n):
      row = list(map(int, input().split()))  # Sửa: đọc cả dòng
      mb.append(row)

  a=[0]*n
  if n==2:
    a[0]=mb[0][1]//2
    a[1]=mb[0][1]//2
  else:
    a[0]=(mb[0][1]+mb[0][2]-mb[1][2])//2
    for i in range(1,n):
      a[i]=mb[0][i]-a[0]
  print(" ".join(map(str,a)))
if __name__=="__main__":
  solve()
