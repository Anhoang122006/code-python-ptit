import math
def is_prime(n):
     if n<2:
         return False
     for i in range(2,int(math.sqrt(n))+1):
         if n%i==0:
             return False
     return True

def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        ans=s[-4:]
        nums=int(ans)
        if is_prime(nums):
            print("YES")
        else:
            print("NO")

if __name__=="__main__":
    solve()
