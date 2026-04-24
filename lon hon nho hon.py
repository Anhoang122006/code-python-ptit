from collections import deque, defaultdict

n = int(input())

mp = {}  # map tên -> id
id_cnt = 0

graph = defaultdict(list)
indegree = defaultdict(int)

def get_id(name):
    global id_cnt
    if name not in mp:
        mp[name] = id_cnt
        id_cnt += 1
    return mp[name]

for _ in range(n):
    a, op, b = input().split()

    u = get_id(a)
    v = get_id(b)

    if op == '>':
        graph[u].append(v)
        indegree[v] += 1
    else:
        graph[v].append(u)
        indegree[u] += 1

# topo sort
q = deque()
for i in range(id_cnt):
    if indegree[i] == 0:
        q.append(i)

cnt = 0
while q:
    u = q.popleft()
    cnt += 1
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print("possible" if cnt == id_cnt else "impossible")
