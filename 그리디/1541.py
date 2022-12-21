#잃어버린 괄호
s = input()
minus = s.split('-')

ans = []
for i in minus:
    if '+' in i:
        plus = i.split('+')
        for j in range(len(plus)):
            plus[j] = int(plus[j])
        ans.append(sum(plus))
    else:
        i = int(i)
        ans.append(i)

new_ans = ans[0]
for i in range(1, len(ans)):
    new_ans -= ans[i]
print(new_ans)
