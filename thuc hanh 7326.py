import math
def solve():
  t=int(input())
  for _ in range(t):
    b=int(input())
    x=input()
    n=0
    pow=0
    string=reversed(x)
    for char in string:
      n+=int(char)*(2**pow)
      pow+=1
    m=n
    result=[]
    while m>0:
      result.append(str(m%b))
      m//=b
    print("".join(reversed(result)))

if __name__=="__main__":
  solve()

