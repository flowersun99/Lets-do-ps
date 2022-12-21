a = int(input())
ans_list = list(map(int, input().split()))
ans = []
while ans_list:
    m = max(ans_list)
    n = min(ans_list)
    b = m - n
    ans.append(b)
    ans_list.remove(m)
    ans_list.remove(n)
    if len(ans_list) == 1:
        ab = ans_list.pop()
        ans.append(ab)
        

print(sum(ans))