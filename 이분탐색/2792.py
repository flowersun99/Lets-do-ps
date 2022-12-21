#보석상자
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x_list = []
for _ in range(m):
    s = int(input())
    x_list.append(s)

lo = 0
hi = 1000000001

def check(x):
    
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(x):
        lo = mid
    else:
        hi = mid