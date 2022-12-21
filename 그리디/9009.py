import sys
input = sys.stdin.readline
t = int(input())
fabo = [0, 1]
for i in range(2, 46):
    fabo.append(fabo[i - 2] + fabo[i - 1])
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(len(fabo) - 1, 0, -1):
        if n >= fabo[i]:
            n -= fabo[i]
            ans.append(fabo[i])
            if n == 0:
                ans.sort()
                print(*ans)