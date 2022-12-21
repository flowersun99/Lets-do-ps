def recursion(s, l, r, q):
    q += 1
    if l >= r: return 1, q
    elif s[l] != s[r]: return 0, q
    else: return recursion(s, l+1, r-1, q)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

n = int(input())

for i in range(n):
    a = input()
    print(*isPalindrome(a))