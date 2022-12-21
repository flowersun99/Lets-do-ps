# 퇴사
import sys
input = sys.stdin.readline
n = int(input())
ans = []
for _ in range(n):
    a = list(map(int, input().split()))
    ans.append(a)
cnt = 0
for i in range(n - 1):
    if i + ans[i][0] > n:
        continue
    elif ans[i][0] == 1:
        cnt += ans[i][0]
        continue
