# 
n , k = map(int,input().split())
number = [ int(input()) for _ in range(n)]
arr = []
flag = 0
cnt = 0
for i in range(n):
    flag = number[flag]
    cnt += 1
    if flag == k:
        break
    
if 0 < cnt < n:
    print(cnt)
else:
    print(-1)