



EXP-1: BFS (Breadth First Search) Pseudocode:

START Initialize Queue with start node Mark start as visited

WHILE Queue not empty: Remove node from Queue Print node

FOR each neighbor:
    IF not visited:
        Mark visited
        Add to Queue
STOP

EXP-2: DFS (Depth First Search)

Pseudocode:

START Take start node

IF node not visited: Print node Mark visited

FOR each neighbor:
    Call DFS(neighbor)
STOP

EXP-3: BFS Traversal Example START Queue ← A Visited ← A

Remove A → print Add B, C

Remove B → print Add D, E

Remove C → print Add F, G

Remove D, E, F, G → print STOP

EXP-4: DFS Traversal Example START Start at A

Go A → B → D Backtrack → E Backtrack → C → F → G STOP

EXP-5: Water Jug Problem (5L & 3L) START (0,0) Fill 5 → (5,0) Pour 5→3 → (2,3) Empty 3 → (2,0) Pour 5→3 → (0,2) Fill 5 → (5,2) Pour 5→3 → (4,3) STOP

EXP-6: DFS Example START 1 → 2 → 4 Backtrack → 5 Backtrack → 3 STOP

EXP-7: DFS Example START 1 → 2 → 4 Backtrack → 5 Backtrack → 3 STOP

EXP-8: General DFS Logic START Use recursion/stack Go deep into graph If dead end → backtrack Continue until goal STOP

EXP-9: Water Jug (5L & 3L) START (0,0) Fill 5 → (5,0) Pour 5→3 → (2,3) Empty 3 → (2,0) Pour 5→3 → (0,2) Fill 5 → (5,2) Pour 5→3 → (4,3) STOP

EXP-10: Water Jug (4L & 3L) START (0,0) Fill 4 → (4,0) Pour 4→3 → (1,3) Empty 3 → (1,0) Pour 4→3 → (0,1) Fill 4 → (4,1) Pour 4→3 → (2,3) STOP

EXP-11: Water Jug (8L, 5L, 3L) START (0,0,8) Pour 8→5 → (0,5,3) Pour 5→3 → (3,2,3) Pour 3→8 → (0,2,6) Pour 5→3 → (2,0,6) Pour 8→5 → (2,5,1) Pour 5→3 → (3,4,1) Pour 3→8 → (0,4,4) STOP

EXP-12: Water Jug (12L, 8L, 5L) START (12,0,0) Pour 12→8 → (4,8,0) Pour 8→5 → (4,3,5) Pour 5→12 → (9,3,0) Pour 3→5 → (9,0,3) Pour 12→8 → (1,8,3) Pour 8→5 → (1,6,5) Pour 5→12 → (6,6,0) STOP
