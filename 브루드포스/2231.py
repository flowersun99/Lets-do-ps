#분해합
n = int(input())
j = n // 10
while True:
    ans = []
    a = str(j)
    for i in a:
        ans.append(int(i))
    if j + sum(ans) == n:
        print(j)
        break
    j += 1
    if j > n:
        print(0)
        break