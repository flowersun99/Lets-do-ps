import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

count = 0
def dfs(v):
    global count
    visited[v] = count
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

for i in range(1, len(visited)):
    print(visited, sep='\n')