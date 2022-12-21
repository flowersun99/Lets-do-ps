import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))

start = 0
last = max(n_list)

while start + 1 < last:
    sum = 0
    mid = (start + last) // 2
    for i in n_list:
        if i - mid > 0:
            sum = sum + (i - mid)
    if sum >= m:
        start = mid
    elif sum < m:
        last = mid

print(start)