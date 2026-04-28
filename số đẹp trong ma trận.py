def solve():
  n,m=map(int,input().split())
  a=[]
  for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
  max_val=-1
  min_val=10e9
  for i in range(n):
    for j in range(m):
      if a[i][j]>max_val:
        max_val=a[i][j]
      if a[i][j]<min_val:
        min_val=a[i][j]
  val=int(max_val-min_val)
  vi_tri=[]
  for i in range(n):
    for j in range(m):
      if a[i][j]==val:
        vi_tri.append((i,j))
  if len(vi_tri)==0:
    print("NOT FOUND")
  else:
    print(val)
    for toa_do in vi_tri:
      print(f"Vi tri [{toa_do[0]}][{toa_do[1]}]")
if __name__=='__main__':
  solve()



