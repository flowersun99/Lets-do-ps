import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

ans = []


for i in m_list:
    start = -1
    end = n - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if n_list[mid] >= i:
            end = mid
        else:
            start = mid

    s = end

    start = 0
    end = n
    while start + 1 < end:
        mid = (start + end) // 2
        if n_list[mid] <= i:
            start = mid
        else:
            end = mid

    e = start

    if i != n_list[s]:
        ans.append(0)
        continue

    cnt = e - s + 1
    ans.append(cnt)
print(*ans)