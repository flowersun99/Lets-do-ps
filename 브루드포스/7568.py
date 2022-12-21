# 덩치치
n = int(input())
ans = []
for _ in range(n):
    new = list(map(int, input().split()))
    ans.append(new)
res = []
for i in range(n):
    cnt = 1
    x = ans[i][0]
    y = ans[i][1]
    for j in range(n):
        if x < ans[j][0] and y < ans[j][1]:
            cnt += 1
    res.append(cnt)
print(*res, sep = ' ')