num_list = [1, 3, 5, 2, 12]

for i in range(len(num_list)):
    for j in range(i):
        print(num_list[i], end=' ')
    print()