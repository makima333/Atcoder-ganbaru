import io
from operator import mod
import sys

_INPUT = """\
.......*
........
........
........
........
........
........
........


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------


col = ["a", "b", "c", "d", "e", "f", "g", "h"]


for r in range(8):
    row = input()
    if row.count("*"):
        for cell_i, cell in enumerate(list(row)):
            if cell == "*":
                print(f"{col[cell_i]}{str(8-r)}")
                exit()
