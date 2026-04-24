def solve():
   t=int(input())
   for i in range(t):
       n = input()
       oke = 0
       for i in range(len(n) - 1):
           if n[i] > n[i + 1]:
               oke = 1
               break
       if oke == 0:
           print("YES")
       else:
           print("NO")


if __name__=="__main__":
    solve()