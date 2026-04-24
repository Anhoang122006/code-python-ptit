def sinh(s,count_A,count_B,count_C,length):
  if len(s)==length:
    if count_A>0 and count_B>0 and count_C>0 and count_A<=count_B<=count_C:
      print(s)
    return
  if count_A< length //3+1:
    sinh(s+'A',count_A+1,count_B,count_C,length)
  sinh(s+'B',count_A,count_B+1,count_C,length)
  sinh(s+'C',count_A,count_B,count_C+1,length)
def solve():
  n=int(input())
  for length in range(3,n+1):
    sinh("",0,0,0,length)

if __name__=="__main__":
  solve()
