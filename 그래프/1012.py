#유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    field[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < height and 0 <= ny < width and field[nx][ny] == 1:
            dfs(nx, ny)

n = int(input())

for _ in range(n):
    width, height, key = map(int, input().split())
    field = [[0] * width for _ in range(height)]
    ans = 0

    for i in range(key):
        a, b = map(int, input().split())
        field[b][a] = 1

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)