s=input()
res=""
count=0
for i in range(len(s)-1,-1,-1):
    res+=s[i]
    count+=1
    if count==3 and i!=0:
        res+=","
        count=0
print(res[::-1])