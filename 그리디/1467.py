import sys
from collections import Counter
input = sys.stdin.readline

seq = input().strip()
R = input().strip()
cnt = Counter(seq) - Counter(R)

ans = ''
idx = 0
while cnt:
    for i in range(9, -1, -1):
        num = str(i)
        if cnt[num] < 1:
            continue
        t = seq.find(num, idx)
        check = cnt - Counter(seq[t:])
        if check:
            continue
        else:
            ans += num
            idx = t + 1
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]
            break
print(ans)