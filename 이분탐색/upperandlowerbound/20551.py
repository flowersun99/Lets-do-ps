#sort 마스터 배지훈의 후계자
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
b = [int(input()) for _ in range(n)]
b.sort()

for _ in range(m):
    d = int(input())
    lo = -1
    hi = len(b) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if b[mid] < d:
            lo = mid
        else:
            hi = mid
    if b[hi] == d:
        print(hi)
    else:
        print(-1)