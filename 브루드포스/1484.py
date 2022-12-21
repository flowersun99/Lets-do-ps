#다이어트
g = int(input())
s = 1
e = 1
cnt = 0
while e <= 100000:
    if int(e ** 2) - int(s ** 2) == g:
        print(e)
        e += 1
        cnt += 1
    elif int(e ** 2) - int(s ** 2) < g:
        e += 1
    else:
        s += 1
if cnt == 0:
    print(-1)