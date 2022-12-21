#좋다
import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
n_list = list(map(int, input().split()))
for i in range(len(n_list)):
    if n_list[i] > 2:
        cnt += 1

print(cnt)