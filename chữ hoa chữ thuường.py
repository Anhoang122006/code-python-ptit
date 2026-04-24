string=input()
count1=0
count2=0
for i in range(len(string)):
    if string[i].islower():
        count1 +=1
    else:
        count2 +=1

if count1>=count2:
    s=string.lower()
else:
    s=string.upper()
print(s)