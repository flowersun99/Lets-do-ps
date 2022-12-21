#용돈관리
n, m = map(int, input().split())
x_list = []
for _ in range(n):
    a = int(input())
    x_list.append(a)

def check(x):
    cnt = 1
    ans = x
    for i in x_list:
        if ans - i < 0:
            ans = x
            cnt += 1
        ans -= i
    return cnt > m or x < max(x_list)

lo = 0
hi = sum(x_list) + 1

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid

print(hi)