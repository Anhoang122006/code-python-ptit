import math
def demuoc(n):
    count=0
    for i in range(1,math.sqrt(n)+1):
        if n%i==0:
            count+=1
            if i*i!=n:
                count+=1
    return count
def solve():
    t=int(input())
    for _ in range(t):
       n=int(input())
