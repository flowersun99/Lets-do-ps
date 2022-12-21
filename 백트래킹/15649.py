import sys
import itertools
input = sys.stdin.readline
n, m = map(int, input().split())
ans = [i for i in range(1, n+1)]
nans = itertools.permutations(ans, m)
for i in nans:
    if i[0] > i[1]:
        continue
    print(*i)