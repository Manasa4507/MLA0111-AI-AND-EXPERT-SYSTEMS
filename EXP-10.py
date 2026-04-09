from collections import deque

def water_jug_3():
    cap = (12, 8, 5)
    start = (12, 0, 0)
    visited = set()
    q = deque([(start, [])])

    while q:
        (a, b, c), path = q.popleft()

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        path = path + [(a, b, c)]

        if a == 6 and b == 6:
            for p in path:
                print(p)
            return

        states = [
            (max(a - (cap[1]-b), 0), min(cap[1], b+a), c),  # A→B
            (max(a - (cap[2]-c), 0), b, min(cap[2], c+a)),  # A→C
            (min(cap[0], a+b), max(b - (cap[0]-a), 0), c),  # B→A
            (a, max(b - (cap[2]-c), 0), min(cap[2], c+b)),  # B→C
            (min(cap[0], a+c), b, max(c - (cap[0]-a), 0)),  # C→A
            (a, min(cap[1], b+c), max(c - (cap[1]-b), 0))   # C→B
        ]

        for s in states:
            q.append((s, path))

water_jug_3()
