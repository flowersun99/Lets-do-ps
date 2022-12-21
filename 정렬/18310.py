n = int(input())
li = list(map(int, input().split()))
li.sort()
print(li[(len(li) // 2) - 1])