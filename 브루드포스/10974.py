import itertools
n = int(input())
ans = [i for i in range(1, n+1)]
nan = itertools.permutations(ans, n)
for i in nan:
    print(*i)