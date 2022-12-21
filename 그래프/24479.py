#24479 알고리즘 수업 dfs-1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8) 

def recu(v, discovered = []):
  visit[v] = True
  discovered.append(v)
  for w in graph[v]:
    if visit[w] == False:
      visit[w] = True
      discovered = recu(w, discovered)
  return discovered

n, m, v = map(int, input().split())

visit = [False] * (n + 1) 

graph = {}
for i in range(n):
  graph[i] = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  if len(graph[i]) == 0:
    pass
  else:
    graph[i].sort()

print(*recu(v), sep='\n')
print(0)

######################이 코드로 했는데 시간초과 남



# def iterative_dfs(start_v):
#   discovered = []
#   stack = deque([start_v])
#   while stack:
#     v = stack.pop()
#     if v not in discovered:
#       discovered.append(v)
#       for w in graph[v]:
#         stack.append(w)
#   return discovered

# n, m, v = map(int, input().split())
# graph = dict()

# for i in range(n+1):
#   graph[i] = list()

# for _ in range(m):
#   a, b = map(int, input().split())
#   graph[a].append(b)
#   graph[b].append(a)
#   graph[a].sort()
#   graph[b].sort()

# print(graph)
# a = iterative_dfs(v)
# for i in range(len(a)):
#   print(a[i])
# print(0)

##정답
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])