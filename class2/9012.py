T = int(input())
for _ in range(T):
    a = input()
    while True:
        if '()' in a:
            a = a.replace('()', '')
        if len(a) <= 3:
            break
    if a == '()':
        print('YES')
    else:
        print('NO')

