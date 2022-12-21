n = int(input())

for _ in range(n):
    right = []
    left = []
    a = input()
    for i in a:
        if i == '(':
            right.append(i)
        else:
            left.append(i)
    if len(right) == len(left):
        print('YES')
    else:
        print('NO')
