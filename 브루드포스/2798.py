# 블랙젝

n, m = map(int, input().split())
ans_list = list(map(int, input().split()))
result = 0

for i in range(len(ans_list)):
    for j in range(i + 1, len(ans_list)):
        for z in range(j + 1, len(ans_list)):
            if m < ans_list[i] + ans_list[j] + ans_list[z]:
                continue
            else:
                result = max(result, ans_list[i] + ans_list[j] + ans_list[z])

print(result)
