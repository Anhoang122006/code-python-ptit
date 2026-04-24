def solve():
   t=int(input())
   for _ in range(t):
       n=input()
       tim_thay=False
       for i in range(1000):
           if int(n)%7==0:
               print(n)
               tim_thay=True
               break

           n_dao=n[::-1]
           tong_dao=int(n)+int(n_dao)
           n=str(tong_dao)
       if tim_thay==False:
           print("-1")
if __name__=="__main__":
    solve()
