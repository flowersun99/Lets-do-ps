#그룹 단어 체커

b = int(input())
ans = b
for _ in range(b):
    a = input()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            pass
        elif a[i] in a[i+1:]:
            ans -= 1
            break
print(ans)