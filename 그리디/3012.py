#등수 매기기
import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
cnt = 0
cor = 1
for i in li:
    if i == cor:
        cor += 1
        continue
    else:
        cnt += abs(cor - i)
        cor += 1

print(cnt)