#두 용액
import sys
input = sys.stdin.readline
n = int(input())
solution = list(map(int, input().split(' ')))

solution.sort()

left = 0
right = n-1

answer = 2e+9+1
final = []

while left < right:
    s = solution[left]
    e = solution[right]

    tot = s + e

    if abs(tot) < answer:
        answer = abs(tot)
        final = [s, e]

    if tot < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])