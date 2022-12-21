#수리공 항승이

n, l = map(int, input().split())

lo = list(map(int, input().split()))

lo.sort()
start = lo[0]
cnt = 1

for i in range(1, len(lo)):
    if lo[i] - start < l:
        continue
    else:
        start = lo[i]
        cnt += 1

print(cnt)