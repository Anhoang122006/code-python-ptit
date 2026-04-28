import math
def snt(n):
  if(n<2):
    return False
  else:
    for i in range(2,int(math.sqrt(n))+1):
      if n%i==0:
        return False
  return True

def solve():
  n,m=map(int,input().split())
  a=[]
  for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
  max_prime=-1
  for i in range(n):
    for j in range(m):
      val=a[i][j]
      if snt(val) and val>max_prime:
        max_prime=val
  if max_prime==-1:
    print("NOT FOUND")
  else:
    print(max_prime)
    for i in range(n):
      for j in range(m):
        if a[i][j]==max_prime:
           print(f"Vi tri [{i}][{j}]")


if __name__ == '__main__':
    solve()

