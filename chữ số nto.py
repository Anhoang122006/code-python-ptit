import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check_prime(n):
    m=len(str(n))
    if not is_prime(m):
        return False
    count1=0
    count2=0
    for i in range(len(str(n))):
        if is_prime(int(str(n)[i])):
            count1+=1
        else:
            count2+=1
    if count1<count2:
        return False

    return True
def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        if check_prime(s):
            print("YES")
        else:
            print("NO")
if __name__=="__main__":
    solve()
