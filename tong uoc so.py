import sys
input=sys.stdin.readline
def solve():
   MAX_VAL=2000001
   uoc_nho_nhat=[0]*(MAX_VAL)
   for i in range(2,1415):
      if uoc_nho_nhat[i]==0: #i la so nguyen to
         for j in range(i*i,MAX_VAL,i):#i la uoc nho nhat cua j
            if uoc_nho_nhat[j]==0:
               uoc_nho_nhat[j]=i
   for i in range(2,MAX_VAL):
        if uoc_nho_nhat[i]==0:
            uoc_nho_nhat[i]=i
   n=int(input().strip())
   tong_tb=0
   for i in range(n):
      x=int(input().strip())
      temp=x
      while temp>1:
         p=uoc_nho_nhat[temp]
         tong_tb+=p
         temp//=p
   print(tong_tb)
if __name__=="__main__":
    solve()
