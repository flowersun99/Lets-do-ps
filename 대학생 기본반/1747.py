#소수 & 펠린드롬
n = int(input())
if n == 2:
    print(2)
    exit()
while True:
    n_str = str(n)
    if n_str != n_str[::-1]:
        n += 1
        continue
    for i in range(2, n):
        if n % i == 0:
            n += 1
            continue
    break
print(n)