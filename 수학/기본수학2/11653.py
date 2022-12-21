#소인수분해

n = int(input())
i = 2
while n != 1:
    if n % i != 0:
        i += 1
        continue
    else:
        while n % i == 0:
            print(i)
            n = n // i
        i += 1