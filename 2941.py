#크로아티아 알파벳 구현
dic = {
    'c=' : 'č',
    'c-' : 'ć',
    'dz=' : '1',
    'd-' : 'đ',
    'lj' : '1'	,
    'nj' : '1',
    's=' : 'š',
    'z=' : 'ž'
}

a = input()
for key, value in dic.items():
  if key in a:
    a = a.replace(key, value)

print(len(a))