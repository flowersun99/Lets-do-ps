n = int(input())
ans = []
for _ in range(n):
    x = list(map(int, input().split()))
    ans.append(x)

ans.sort(key= lambda x : (x[1], x[0]))
for i, v in ans:
    print(i, v)