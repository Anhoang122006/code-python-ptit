import sys
from itertools import combinations

def solve():
    data = []
    while len(data) < 12:
        data += sys.stdin.read().split()
    w = list(map(int, data[:12]))

    indices = list(range(12))
    best = float('inf')

    for g1 in combinations(indices, 3):
        s1 = set(g1)
        rem1 = [i for i in indices if i not in s1]
        for g2 in combinations(rem1, 3):
            s2 = set(g2)
            rem2 = [i for i in rem1 if i not in s2]
            for g3 in combinations(rem2, 3):
                s3 = set(g3)
                g4 = tuple(i for i in rem2 if i not in s3)

                sums = [
                    sum(w[i] for i in g1),
                    sum(w[i] for i in g2),
                    sum(w[i] for i in g3),
                    sum(w[i] for i in g4),
                ]
                diff = max(sums) - min(sums)
                if diff < best:
                    best = diff

    print(best)

solve()
