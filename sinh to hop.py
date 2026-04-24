def solve():
   n,k=map(int,input().split())
   a=list(map(int,input().split()))
   a_unique=sorted(list(set(a)))
   m=len(a_unique)
   x=[0]*k
   def Try(i,start):
      for j in range(start,m):
         x[i]=a_unique[j]
         if i==k-1:
            print(*x) # * để in ra các phần tử của x cách nhau một khoảng trắng
         else:
            Try(i+1,j+1)
    Try(0,0)

if __name__ == "__main__":
   solve()
