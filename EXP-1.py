from collections import deque

def bfs(g, s):
    v, q = set([s]), deque([s])
    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in g[n]:
            if i not in v:
                v.add(i)
                q.append(i)

g = {'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
bfs(g,'A')
