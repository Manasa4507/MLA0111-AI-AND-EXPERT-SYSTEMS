def dfs(g, n, v=set()):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(g, i, v)

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

dfs(g, 'A')
