from collections import deque
def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        q=deque(['2','4','6','8'])
        res=[]
        while True:
            half=q.popleft()
            full=half+half[::-1]
            if int(full)>=n:
                break
            res.append(full)
            for digit in "02468":
                q.append(half+digit)

        m=len(res)
        for i in range(m):
            if i<m-1:
                print(res[i],end=" ")
            else:
                print(res[i])

if __name__=="__main__":
    solve()

