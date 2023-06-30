import sys
from collections import deque
input = sys.stdin.readline

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]


def bfs(a, b, graph):
    cnt = 1
    graph[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            if graph[dx][dy] == 1:
                graph[dx][dy] = 0
                cnt += 1
                queue.append((dx, dy))
    return cnt

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(bfs(i, j, graph))

print(len(ans))

print(max(ans)) if ans else print(0)