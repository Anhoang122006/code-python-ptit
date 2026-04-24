def thap_hn(n,nguon,trung_gian,dich):
        if n==1:
            print(f"{nguon} -> {dich}")
            return
        #chuyển nguồn sang trung gian
        thap_hn(n-1,nguon,dich,trung_gian)
        print(f"{nguon} -> {dich}")
        thap_hn(n-1,trung_gian,nguon,dich)
def solve():
    n=int(input())
    thap_hn(n,'A','B','C')

if __name__=="__main__":
    solve()

