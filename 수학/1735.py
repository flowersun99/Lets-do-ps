import math
a, b = map(int, input().split())
c, d = map(int, input().split())

son = a * d + c * b
mom = b * d

num = math.gcd(son, mom)
print(int(son / num), int(mom / num))
