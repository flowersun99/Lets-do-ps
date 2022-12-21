#단어 수학
import sys
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in  range(n)]
dict = {}

for word in words:
    power = len(word)-1
    for c in word:
        if c in dict:
            dict[c] += pow(10, power)
        else:
            dict[c] = pow(10, power)
        power -= 1

dict = sorted(dict.values(), reverse=True)

answer = 0
mul = 9
for i in dict:
    answer += mul * i
    mul -= 1

print(answer)