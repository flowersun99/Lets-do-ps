a, b = map(int, input().split())
not_heard = []
not_see = []
for _ in range(a):
    nh = input()
    not_heard.append(nh)

for _ in range(b):
    ns = input()
    not_see.append(ns)

not_heard = set(not_heard)
not_see = set(not_see)
ans = not_heard & not_see
ans = list(ans)
ans.sort()

print(len(ans))
print(*ans, sep='\n')