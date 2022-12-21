n = int(input())

count = 0
i = 0
plus = 1
while i <= n:
    i += plus
    plus += 1
    count += 1

print(count-1)