BFS AND DFS
EXP-1

START
Insert starting node into Queue
Mark it visited
Remove node → print
Add its neighbors
Repeat until queue empty
STOP
EXP-2

START
Take starting node
Print node
Mark visited
Visit all adjacent nodes using recursion
STOP
EXP-3

START
Queue ← A
Visit A → add B,C
Visit B → add D,E
Visit C → add F,G
Visit remaining nodes
STOP
EXP-4

START
A → B → D
Backtrack → E
Backtrack → C → F → G
STOP
EXP-5

START
Queue ← 1
Visit 1 → add 2,3
Visit 2 → add 4,5
Visit 3
Visit 4,5
STOP
EXP-6

START
1 → 2 → 4
Backtrack → 5
Backtrack → 3
STOP
EXP-7

START
Begin at 1
Go to 2 → then 4
Backtrack → 5
Backtrack → 3
STOP
EXP-8

START
Use recursion/stack
Traverse deep into graph
If dead end → backtrack
Continue until complete
STOP
WATER JUG
EXP-9

START
(0,0)
Fill 5 → (5,0)
Pour 5→3 → (2,3)
Empty 3 → (2,0)
Pour 5→3 → (0,2)
Fill 5 → (5,2)
Pour 5→3 → (4,3)
STOP
EXP-10

START
(0,0)
Fill 4 → (4,0)
Pour 4→3 → (1,3)
Empty 3 → (1,0)
Pour 4→3 → (0,1)
Fill 4 → (4,1)
Pour 4→3 → (2,3)
STOP
EXP-11

START
(0,0,8)
Pour 8→5 → (0,5,3)
Pour 5→3 → (3,2,3)
Pour 3→8 → (0,2,6)
Pour 5→3 → (2,0,6)
Pour 8→5 → (2,5,1)
Pour 5→3 → (3,4,1)
Pour 3→8 → (0,4,4)
STOP
EXP-12

START
(12,0,0)
Pour 12→8 → (4,8,0)
Pour 8→5 → (4,3,5)
Pour 5→12 → (9,3,0)
Pour 3→5 → (9,0,3)
Pour 12→8 → (1,8,3)
Pour 8→5 → (1,6,5)
Pour 5→12 → (6,6,0)
STOP
