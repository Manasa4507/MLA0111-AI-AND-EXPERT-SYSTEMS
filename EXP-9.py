from collections import deque

def water_jug(a, b, target):
    v = set()
    q = deque([((0, 0), [])])

    while q:
        (x, y), p = q.popleft()
        if (x, y) in v:
            continue
        v.add((x, y))
        p = p + [(x, y)]

        if x == target or y == target:
            for i in p:
                print(i)
            return

        q.append(((a, y), p))
        q.append(((x, b), p))
        q.append(((0, y), p))
        q.append(((x, 0), p))

        t = min(x, b - y)
        q.append(((x - t, y + t), p))

        t = min(y, a - x)
        q.append(((x + t, y - t), p))

water_jug(5, 3, 4)
