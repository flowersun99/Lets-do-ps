n = int(input())
ans = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    nlist = list()
    nlist.append(a)
    nlist.append(b)
    nlist.append(i)
    ans.append(nlist)
ans.sort(key=lambda x : (x[0], x[2]))
for a, b, c in ans:
    print(a, b)