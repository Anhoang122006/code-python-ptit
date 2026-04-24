class rectangle:
    def __init__(self,chieu_dai,chieu_rong,mau_sac):
        self.chieu_dai= chieu_dai
        self.chieu_rong=chieu_rong
        self.mau_sac=mau_sac
    def chu_vi(self):
        return (self.chieu_dai+self.chieu_rong)*2
    def dien_tich(self):
        return self.chieu_rong*self.chieu_dai
    def color(self):
        return self.mau_sac
def solve():
    l, w, c = input().split()
    if l>0 and w>0:
        react=rectangle(l,w,c)
        print(f"{react.chu_vi()}{react.dien_tich()}{react.color()}")
    else:
        print("INVALID")
if __name__=="__main__":
    solve()

