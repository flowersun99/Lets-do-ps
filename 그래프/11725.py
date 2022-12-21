#트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

def dfs(graph, parent, start):
    for i in graph[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(graph, parent, i)

dfs(graph, parent, 1)

for i in range(2, n+1):
    print(parent[i])
