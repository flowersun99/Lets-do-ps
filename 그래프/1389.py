#케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
ans = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        graph[v].sort()
        for g in graph[v]:
            if visited[g] == 0:
                visited[g] += visited[v] + 1
                q.append(g)

res = []
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res)) + 1)