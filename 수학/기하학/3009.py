x_list = []
y_list = []
ans_list = []
for _ in range(3):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        ans_list.append(x_list[i])

for j in range(3):
    if y_list.count(y_list[j]) == 1:
        ans_list.append(y_list[j])

print(*ans_list)
