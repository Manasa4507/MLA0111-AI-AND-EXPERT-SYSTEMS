from collections import deque

def jug():
    cap = (4,9,11)
    q = deque([((0,0,11), [])])
    v = set()

    while q:
        (a,b,c), p = q.popleft()
        if (a,b,c) in v: continue
        v.add((a,b,c))
        p = p + [(a,b,c)]

        if b==5 and c==6:
            for i in p: print(i)
            return

        t=min(a,cap[1]-b); q.append(((a-t,b+t,c),p))
        t=min(a,cap[2]-c); q.append(((a-t,b,c+t),p))
        t=min(b,cap[0]-a); q.append(((a+t,b-t,c),p))
        t=min(b,cap[2]-c); q.append(((a,b-t,c+t),p))
        t=min(c,cap[0]-a); q.append(((a+t,b,c-t),p))
        t=min(c,cap[1]-b); q.append(((a,b+t,c-t),p))

jug()
