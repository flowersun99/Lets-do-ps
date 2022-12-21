n = int(input())
n_list = [input() for _ in range(n)]
n_list = list(set(n_list))
n_list.sort(key = lambda x : (len(x), x))
print(*n_list, sep='\n')