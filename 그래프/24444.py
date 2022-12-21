#알고리즘 수업 bfs - 1
from collections import deque
import sys
input = sys.stdin.readline

# def iterative_bfs(start_v):
#   discovered = deque([start_v])
#   queue = [start_v]
#   while queue:
#     v = queue.pop(0)
#     for w in graph[v]:
#       if w not in discovered:
#         discovered.append(w)
#         queue.append(w)
#   return discovered

def iterative_bfs(graph, r, visited):
  queue = deque([r])
  visited[r] = 1
  count = 2
  while queue:
    r = queue.popleft()
    for i in graph[r]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = count
        count += 1

n, m, v = map(int, input().split())

# graph = {}
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n + 1):
  graph[i].sort()

iterative_bfs(graph, v, visited)
print(graph)
print(visited)
for i in visited[1::]:
  print(i)