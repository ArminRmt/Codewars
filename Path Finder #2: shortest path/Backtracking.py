
# Backtracking
# Time complexity: O(4^MN)

import sys
import math


class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y


def isSafe(mat, visited, x, y):
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 1 and (not visited[x][y]))


def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):
    if (i == x and j == y):
        min_dist = min(dist, min_dist)
        return min_dist

    # set (i, j) cell as visited
    visited[i][j] = True

    # go to the bottom cell
    if (isSafe(mat, visited, i + 1, j)):
        min_dist = findShortestPath(
            mat, visited, i + 1, j, x, y, min_dist, dist + 1)

    # go to the right cell
    if (isSafe(mat, visited, i, j + 1)):
        min_dist = findShortestPath(
            mat, visited, i, j + 1, x, y, min_dist, dist + 1)

    # go to the top cell
    if (isSafe(mat, visited, i - 1, j)):
        min_dist = findShortestPath(
            mat, visited, i - 1, j, x, y, min_dist, dist + 1)

    # go to the left cell
    if (isSafe(mat, visited, i, j - 1)):
        min_dist = findShortestPath(
            mat, visited, i, j - 1, x, y, min_dist, dist + 1)

    visited[i][j] = False  # backtrack: remove (i, j) from the visited matrix

    return min_dist


def findShortestPathLength(mat, src, dest):
    if (len(mat) == 0 or mat[src.first][src.second] == 0 or mat[dest.first][dest.second] == 0):
        return -1

    row = len(mat)
    col = len(mat[0])

    # construct an `M × N` matrix to keep track of visited
    # cells
    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])

    dist = sys.maxsize
    dist = findShortestPath(mat, visited, src.first,
                            src.second, dest.first, dest.second, dist, 0)

    if (dist != sys.maxsize):
        return dist
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

    src = Pair(0, 0)
    dest = Pair(3, 4)
    dist = findShortestPathLength(mat, src, dest)
    if (dist != -1):
        return dist

    else:
        return False
