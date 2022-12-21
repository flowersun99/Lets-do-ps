import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n_list = []
for i in range(a):
    c = int(input())
    n_list.append(c)
if a == b:
    print(0)
    exit(0)
start = 1
end = int(1e10)

while start + 1 < end: # +1 이부분
    sum = 0
    mid = (start + end) // 2
    for i in n_list:
        sum += i // mid
    if sum < b:   
        end = mid # end = mid - 1
    else:
        start = mid #start = mid + 1 이렇게 왜 해야함?

print(start)