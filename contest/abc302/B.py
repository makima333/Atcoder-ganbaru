import io
from operator import mod
import sys

_INPUT = """\
5 5
skuns
sssns
ssusu
sksuk
essse


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())
snuke = ["s", "n", "u", "k", "e"]

cells = [list(input()) for _ in range(h)]


for r_i, row in enumerate(cells):
    for c_i, cell in enumerate(row):
        if cell == "s":
            # yoko
            if c_i + 4 <= w - 1:
                if (
                    cells[r_i][c_i + 1] == snuke[1]
                    and cells[r_i][c_i + 2] == snuke[2]
                    and cells[r_i][c_i + 3] == snuke[3]
                    and cells[r_i][c_i + 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1, c_i + 1 + 1)
                    print(r_i + 1, c_i + 2 + 1)
                    print(r_i + 1, c_i + 3 + 1)
                    print(r_i + 1, c_i + 4 + 1)
                    exit()
            if c_i - 4 >= 0:
                if (
                    cells[r_i][c_i - 1] == snuke[1]
                    and cells[r_i][c_i - 2] == snuke[2]
                    and cells[r_i][c_i - 3] == snuke[3]
                    and cells[r_i][c_i - 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1, c_i - 1 + 1)
                    print(r_i + 1, c_i - 2 + 1)
                    print(r_i + 1, c_i - 3 + 1)
                    print(r_i + 1, c_i - 4 + 1)
                    exit()
            # tate
            if r_i + 4 <= h - 1:
                if (
                    cells[r_i + 1][c_i] == snuke[1]
                    and cells[r_i + 2][c_i] == snuke[2]
                    and cells[r_i + 3][c_i] == snuke[3]
                    and cells[r_i + 4][c_i] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 + 1, c_i + 1)
                    print(r_i + 1 + 2, c_i + 1)
                    print(r_i + 1 + 3, c_i + 1)
                    print(r_i + 1 + 4, c_i + 1)
                    exit()
            if r_i - 4 >= 0:
                if (
                    cells[r_i - 1][c_i] == snuke[1]
                    and cells[r_i - 2][c_i] == snuke[2]
                    and cells[r_i - 3][c_i] == snuke[3]
                    and cells[r_i - 4][c_i] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 - 1, c_i + 1)
                    print(r_i + 1 - 2, c_i + 1)
                    print(r_i + 1 - 3, c_i + 1)
                    print(r_i + 1 - 4, c_i + 1)
                    exit()
            # naname
            if c_i + 4 <= w - 1 and r_i + 4 <= h - 1:
                if (
                    cells[r_i + 1][c_i + 1] == snuke[1]
                    and cells[r_i + 2][c_i + 2] == snuke[2]
                    and cells[r_i + 3][c_i + 3] == snuke[3]
                    and cells[r_i + 4][c_i + 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 + 1, c_i + 1 + 1)
                    print(r_i + 1 + 2, c_i + 1 + 2)
                    print(r_i + 1 + 3, c_i + 1 + 3)
                    print(r_i + 1 + 4, c_i + 1 + 4)
                    exit()
            if c_i - 4 >= 0 and r_i - 4 >= 0:
                if (
                    cells[r_i - 1][c_i - 1] == snuke[1]
                    and cells[r_i - 2][c_i - 2] == snuke[2]
                    and cells[r_i - 3][c_i - 3] == snuke[3]
                    and cells[r_i - 4][c_i - 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 - 1, c_i + 1 - 1)
                    print(r_i + 1 - 2, c_i + 1 - 2)
                    print(r_i + 1 - 3, c_i + 1 - 3)
                    print(r_i + 1 - 4, c_i + 1 - 4)
                    exit()
            if r_i + 4 <= h - 1 and c_i - 4 >= 0:
                if (
                    cells[r_i + 1][c_i - 1] == snuke[1]
                    and cells[r_i + 2][c_i - 2] == snuke[2]
                    and cells[r_i + 3][c_i - 3] == snuke[3]
                    and cells[r_i + 4][c_i - 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 + 1, c_i + 1 - 1)
                    print(r_i + 1 + 2, c_i + 1 - 2)
                    print(r_i + 1 + 3, c_i + 1 - 3)
                    print(r_i + 1 + 4, c_i + 1 - 4)
                    exit()
            if r_i + 4 >= 0 and c_i + 4 <= w - 1:
                if (
                    cells[r_i - 1][c_i + 1] == snuke[1]
                    and cells[r_i - 2][c_i + 2] == snuke[2]
                    and cells[r_i - 3][c_i + 3] == snuke[3]
                    and cells[r_i - 4][c_i + 4] == snuke[4]
                ):
                    print(r_i + 1, c_i + 1)
                    print(r_i + 1 - 1, c_i + 1 + 1)
                    print(r_i + 1 - 2, c_i + 1 + 2)
                    print(r_i + 1 - 3, c_i + 1 + 3)
                    print(r_i + 1 - 4, c_i + 1 + 4)
                    exit()
