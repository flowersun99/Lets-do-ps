#섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [0, -1, 1, 0, 1, -1, 1, -1]
    field[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < height and 0 <= ny < width and field[nx][ny] == 1:
            dfs(nx, ny)

while True:
    width, height = map(int, input().split())
    if width == 0 and height == 0:
        break

    field = []
    ans = 0

    for i in range(height):
        li = list(map(int, input().split()))
        field.append(li)

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)