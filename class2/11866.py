#요세푸스 문제0
from collections import deque
li = deque()
ans = []
n, k = map(int, input().split())
for i in range(1, n+1):
    li.append(i)


while li:
    for i in range(k-1):
        li.append(li.popleft())
    ans.append(li.popleft())

print('<', end = '')
for i in range(n - 1):
    print(f'{ans[i]}, ', end='')
print(ans[-1], end='')
print('>')