#기타레슨
n, m = map(int, input().split())
gui = list(map(int, input().split()))

def check(x):
    if x < t:
        return False

    cnt = 1
    ans = x
    for i in gui:
        if ans - i < 0:
            cnt += 1
            ans = x
        ans -= i

    
    return cnt <= m

t = max(gui)
lo = 0
hi = sum(gui)

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)