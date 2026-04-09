def dfs(g, n, v=set()):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(g, i, v)

g = {
    0:[1],
    1:[3],
    2:[1],
    3:[2,4],
    4:[5],
    5:[7],
    6:[],
    7:[6]
}

dfs(g, 0)
