from collections import deque
import sys
input = sys.stdin.readline

visited = [0] * 5
graph = [[] for i in range(5)]

#bfs
def bfs(v):
    global count
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        graph[v].sort()
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)

#dfs
def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)