n = input()
li = [int(i) for i in n]
li.sort(reverse=True)
nli = [str(i) for i in li]
print(''.join(nli))