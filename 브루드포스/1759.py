#암호 만들기
import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
alph = list(map(str, input().split()))
alph.sort()
comb = combinations(alph, l)
moum = ['a', 'e', 'i', 'o', 'u']
res = []
for c in comb:
    j = 0
    m = 0
    for i in range(l):
        if c[i] in moum:
            m += 1
        else:
            j += 1
    if m>=1 and j>=2:
        print(''.join(c))