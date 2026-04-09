from queue import PriorityQueue

def best_first(graph, start, goal, h):
    v = set()
    pq = PriorityQueue()
    pq.put((h[start], start))

    while not pq.empty():
        _, n = pq.get()
        if n not in v:
            print(n, end=" ")
            v.add(n)

            if n == goal:
                break

            for i in graph[n]:
                if i not in v:
                    pq.put((h[i], i))

g = {'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
h = {'A':3,'B':2,'C':1,'D':0,'E':0}

best_first(g, 'A', 'E', h)
