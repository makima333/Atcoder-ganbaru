import io
from operator import mod
import sys

_INPUT = """\
5
01010
01001
10110
00110
01010


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

grid = [list(input()) for _ in range(n)]


def rotate_outer(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rotated_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                if i == 0 and j != 0:
                    rotated_matrix[i][j] = matrix[i][j - 1]
                    continue

                if j == 0 and i != rows - 1:
                    rotated_matrix[i][j] = matrix[i + 1][j]
                    continue

                if i == rows - 1 and j != cols - 1:
                    rotated_matrix[i][j] = matrix[i][j + 1]
                    continue

                if j == cols - 1 and i != 0:
                    rotated_matrix[i][j] = matrix[i - 1][j]
                    continue

            else:
                rotated_matrix[i][j] = matrix[i][j]

    return rotated_matrix


for row in rotate_outer(grid):
    print("".join(row))
