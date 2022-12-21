#자유이용권
import sys
import math
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

if sum(li) % 2 == 0:
    z = sum(li) // 2
else:
    z = sum(li) // 2 + 1

if z >= max(li):
    print(sum(li))
else:
    print((sum(li) - max(li)) * 2 + 1)