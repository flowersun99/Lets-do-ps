import sys
input = sys.stdin.readline

n = int(input())
ans = list(map(int, input().split()))
m = int(input())
if sum(ans) <= m:
    print(max(ans))
    exit()
start = 0
end = 1000000

while start + 1 < end:
    sum = 0
    mid = (start + end) // 2
    for i in ans:
        if i - mid > 0:
            sum += mid
        else:
            sum += i
    if sum <= m:
        start = mid
    else:
        end = mid

print(start)