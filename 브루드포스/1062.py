# a, n, t, i, c
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [input() for _ in range(n)]
new_ans = []

for i in li:
    for j in i:
        ans = []
        ans.append(j)
    new_ans.append(ans)

