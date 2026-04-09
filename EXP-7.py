def dfs(g, n, v=set()):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(g, i, v)

g = {
    1:[2,7],
    2:[3,6],
    3:[4,5],
    4:[],
    5:[],
    6:[],
    7:[8,10],
    8:[9],
    9:[],
    10:[]
}

dfs(g, 1)
