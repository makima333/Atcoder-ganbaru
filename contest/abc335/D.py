import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
9



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())


def create_spiral_matrix(n, center_value):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Starting values
    num = 1
    x, y = 0, 0
    dx, dy = 0, 1  # Initial direction

    for _ in range(n * n):
        # Assign the value and move
        matrix[x][y] = num
        num += 1

        # Check for direction change
        if (
            x + dx >= n
            or y + dy >= n
            or x + dx < 0
            or y + dy < 0
            or matrix[x + dx][y + dy] != 0
        ):
            dx, dy = dy, -dx  # Change direction

        x += dx
        y += dy

    # Set the center value
    center_index = n // 2
    matrix[center_index][center_index] = center_value

    return matrix


# Create a 5x5 spiral matrix with 'T' in the center
spiral_matrix = create_spiral_matrix(N, "T")

# Display the matrix
for row in spiral_matrix:
    print(" ".join(map(str, row)))
