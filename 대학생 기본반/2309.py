ans = []

for _ in range(9):
    a = int(input())
    ans.append(a)

b = sum(ans)

for i in range(len(ans) - 1):
    for j in range(i + 1, len(ans)):
        num1 = ans[i]
        num2 =  ans[j]
        if b - (num1 + num2) == 100:
            ans.remove(num1)
            ans.remove(num2)
            ans.sort()
            print(*ans, sep='\n')
            exit(0)