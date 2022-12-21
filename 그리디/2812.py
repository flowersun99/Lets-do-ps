#크게 만들기
N, K = map(int, input().split())
li = list(input())
k, stack = K, []
for i in range(N):
    while k > 0 and stack and stack[-1] < li[i]:
        stack.pop()
        k -= 1
    stack.append(li[i])
print(''.join(stack[:N-K]))