n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, 0, -1): # 맨 뒤 값부터 시작
    if data[i-1] < data[i]:
        for j in range(n-1, 0, -1): # 다시 맨 뒤 값부터 큰 값찾기
            if data[i-1] < data[j]:
                data[i-1], data[j] = data[j], data[i-1] # 둘 값을 swap
                data = data[:i] + sorted(data[i:])
                for i in data:
                    print(i, end=' ')
                exit()
print(-1)