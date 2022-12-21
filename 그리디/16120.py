#ppap

s = input()
stack = []
for i in range(len(s)):
	stack.append(s[i])
	if stack[-1] == 'P' and stack[-4: ] == list('PPAP'):
		del stack[-4: ]
		stack.append('P')
 
if stack == list('PPAP') or stack == list('P'):
	print('PPAP')
else:
	print('NP')
