def check_stn(n):
  s=str(n)
  return len(s)>=2 and s==s[::-1]
def solve():
  n,m=map(int,input().split())
  a=[]
  for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
  max_stn=-1
  for i in range(n):
    for j in range(m):
      val=a[i][j]
      if val>max_stn and check_stn(val):
        max_stn=val
  if max_stn==-1:
    print("NOT FOUND")
  else:
    print(max_stn)
    for i in range(n):
      for j in range(m):
        if a[i][j]==max_stn:
           print(f"Vi tri [{i}][{j}]")

if __name__=="__main__":
  solve()



