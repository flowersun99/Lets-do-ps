#흙길 보수하기
import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())

pools = []
for _ in range(N):
    pools.append(list(map(int, input().split())))
pools.sort(key=lambda x: x[0])

plankCount = 0
maxPlankIndex = 0

for s, e in pools:
    if s <= maxPlankIndex:
        s = maxPlankIndex+1

        if e <= s:
            continue

    curPlankCount = math.ceil((e-s)/L)
    plankCount += curPlankCount
    maxPlankIndex = max(maxPlankIndex, s + curPlankCount*L-1)

print(plankCount)