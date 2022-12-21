# 5052 전화번호 목록
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    phone = [input().rstrip() for _ in range(n)]
    phone.sort()

    for i in range(n-1):
        length = len(phone[i])
        if phone[i] == phone[i+1][:length]:
            print('NO')
            break
    else:
        print('YES')