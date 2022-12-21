s = input()
t = input()

while True:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
    if t == s:
        print(1)
        exit()
    if len(t) == 1:
        print(0)
        exit()