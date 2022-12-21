import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
loc = list(map(int, input().split()))
# mid = 휴개소의 위치
loc.sort()
lo = 0
hi = l + 1
def check(x):
    

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid