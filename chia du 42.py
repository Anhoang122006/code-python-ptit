import math
import sys
def solve():
  a= sys.stdin.read().split()
  ans=set()
  for i in range(10):
    so=int(a[i])
    du=so%42
    ans.add(du)
  print(len(ans))

if __name__ == "__main__":
    solve()
