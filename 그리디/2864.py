#5와 6의 차이
a, b = map(int, input().split())

max_b = str(b)
if '5' in max_b:
    max_b = max_b.replace('5', '6')
max_a = str(a)
if '5' in max_a:
    max_a = max_a.replace('5', '6')
max_num = int(max_b) + int(max_a)

min_a = str(a)
min_b = str(b)
if '6' in min_a:
    min_a = min_a.replace('6', '5')
if '6' in min_b:
    min_b = min_b.replace('6', '5')

min_num = int(min_b) + int(min_a)

print(min_num, max_num)