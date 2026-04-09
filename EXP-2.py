def dfs(g, n, v=set()):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(g, i, v)

g = {'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
dfs(g, 'A')
