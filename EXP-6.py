def dfs(g, n, v=set()):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(g, i, v)

g = {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[],
    5:[]
}

dfs(g, 1)
