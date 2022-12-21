import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return visited


for i in range(1, n):
    if list(bfs(graph, i, visited)) == list(bfs(graph, i + 1, visited)):
        pass
    else:
        ans += 1

print(ans)