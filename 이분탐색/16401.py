# 과자 나눠주기
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
snack = list(map(int, input().split()))
lo = 0
hi = 1000000001

def check(num):
    cnt = 0
    for i in snack:
        cnt += i // num
    return cnt >= m

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)