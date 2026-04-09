from collections import deque

def bfs(g, s):
    v = set([s])
    q = deque([s])

    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in g[n]:
            if i not in v:
                v.add(i)
                q.append(i)

g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bfs(g, 'A')
