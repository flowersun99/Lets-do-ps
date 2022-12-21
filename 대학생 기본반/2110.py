#공유기 설치
import sys
input = sys.stdin.readline
n, c = map(int, input().split())

x_list = []
for _ in range(n):
    a = int(input())
    x_list.append(a)
x_list.sort()

lo = 0
hi = 1000000001

def check(x):
    find = x_list[0]
    cnt = 1
    for i in range(1, n):
        if x_list[i] - find >= x:
            cnt += 1
            find = x_list[i]
    return cnt >= c
    
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)