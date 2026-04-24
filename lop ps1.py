import math
class phan_so:
    def __init__(self,tu_so,mau_so):
        self.tu_so=tu_so
        self.mau_so=mau_so
    def toi_gian(self):
        g=math.gcd(self.tu_so,self.mau_so)
        self.tu_so//=g
        self.mau_so//=g
    def in(self):
        print(f"{self.tu_so}/{self.mau_so}")

def solve():
    tuso,mauso=map(int,input().split())
    ps=phan_so(tuso,mauso)
    ps.toi_gian()
    ps.in()
if __name__=="__main__":
    solve():nclass Matrix:

    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt

    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.mt[i][k] * self.mt[j][k]
        return Matrix(self.n, self.m, res)

    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''


for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    mt = []
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    matrix = Matrix(n, m, mt)
    print(matrix.__mul__())
