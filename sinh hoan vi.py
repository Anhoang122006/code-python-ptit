import sys
from itertools import permutations
def solve():
  s=input()
  for p in permutations(s):
    print("".join(p))
if __name__ == "__main__":
  solve()
