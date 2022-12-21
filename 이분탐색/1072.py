a, b = map(int, input().split())

z = (b*100)//a

if z >= 99:
    print(-1)
    exit()

start = 0
end = 1000000000

while start + 1 < end:
    mid = (start + end) // 2
    tmp = ((b+mid)*100) // (a+mid)

    if tmp > z:
        end = mid
    else:
        start = mid

print(end)