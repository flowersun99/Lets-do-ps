import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
a.sort()
for i in range(len(m_list)):
    lo = -1
    hi = len(a) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if a[mid] < m_list[i]:
            lo = mid
        else:
            hi = mid
    if m_list[i] == a[hi]:
        print(1)
    else:
        print(0)