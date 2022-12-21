# A -> B
a, b = map(int, input().split())

cnt = 1
while b != a:
    if b % 2 != 0:
        b = (b - 1) / 10
        cnt += 1
    elif b % 2 == 0:
        b = b / 2
        cnt += 1
    if b < a:
        print(-1)
        exit()
print(cnt)