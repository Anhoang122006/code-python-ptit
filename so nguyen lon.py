import math
def solve():
  t=int(input())
  for _ in range(t):
    a=int(input())
    b=int(input())
    n=int(math.gcd(a,b))
    print(n)
if __name__=="__main__":
  solve()
