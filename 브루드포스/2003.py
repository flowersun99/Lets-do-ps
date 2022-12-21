n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cor = 0
    flag = i
    while cor < m:
        if flag >= n:
            break
        cor += li[flag]
        if cor == m:
            cnt += 1
            break
        flag += 1
print(cnt)