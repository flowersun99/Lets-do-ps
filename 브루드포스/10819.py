ans = ['H', 'I', 'A', 'R', 'C']
b = int(input())
a = input()
cnt = []
for i in ans:
    c = a.count(i)
    cnt.append(c)

print(min(cnt))