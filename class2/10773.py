#제로
n = int(input())
ans_list = []
for i in range(n):
    a = int(input())
    if a == 0:
        ans_list.pop(-1)
    else:
        ans_list.append(a)

print(sum(ans_list))