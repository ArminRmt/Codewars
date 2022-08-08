
# Expected time complexity is O(MN)

from collections import deque
import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist


def isValid(row: int, col: int, ROW: int, COL: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def BFS(mat, src: Point, dest: Point, n):

    # check if we have an answer
    if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
        return -1

    visited = [[False for i in range(n)]
               for j in range(n)]

    visited[src.x][src.y] = True

    q = deque()

    s = queueNode(src, 0)
    q.append(s)  # Enqueue cell

    # Do a BFS starting from source cell
    while q:

        curr = q.popleft()  # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col, n, n) and mat[row][col] == 1 and not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col),
                                    curr.dist+1)
                q.append(Adjcell)

    # Return -1 if destination cannot be reached
    return -1


def path_finder(maze):

    input_list = list(maze)
    for x in input_list:
        if x in '\n':
            input_list.remove(x)

    n = int(math.sqrt(len(input_list)))
    mat = [input_list[i:i+n] for i in range(0, len(input_list), n)]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '.':
                mat[i][j] = 1
            else:
                mat[i][j] = 0

    source = Point(0, 0)
    dest = Point(n-1, n-1)

    dist = BFS(mat, source, dest, n)

    if dist != -1:
        return dist
    else:
        return False


# BFS and queue(fifo)

#     from collections import deque

#     graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E', 'F'],
#     'C' : ['G'],
#     'D' : [],
#     'E' : [],
#     'F' : ['H'],
#     'G' : ['I'],
#     'H' : [],
#     'I' : []
#     }

#     def bfs(graph, node):
#         visited = []
#         queue = deque()

#         visited.append(node)
#         queue.append(node)

#         while queue:
#             s = queue.popleft()
#             print(s, end = " ")

#             for n in graph[s]:
#                 if n not in visited:
#                     visited.append(n)
#                     queue.append(n)

#     def main():
#         bfs(graph, 'A')

#     main()
