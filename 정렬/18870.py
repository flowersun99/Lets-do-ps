import sys
input = sys.stdin.readline
n = int(input())
x_list = list(map(int, input().split()))
nx_list = sorted(list(set(x_list)))
d = dict()
for i, v in enumerate(nx_list):
    d[v] = i

for i in x_list:
    print(d[i], end = ' ')