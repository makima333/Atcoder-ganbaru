import io
from operator import mod
import sys

_INPUT = """\
15 20
#.#..#.............#
.#....#....#.#....#.
#.#....#....#....#..
........#..#.#..#...
#.....#..#.....#....
.#...#....#...#..#.#
..#.#......#.#....#.
...#........#....#.#
..#.#......#.#......
.#...#....#...#.....
#.....#..#.....#....
........#.......#...
#.#....#....#.#..#..
.#....#......#....#.
#.#..#......#.#....#


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())
cells = [list(input()) for _ in range(h)]
N = min(h, w)
ans = [0 for _ in range(N)]

for y, rows in enumerate(cells):
    for x, cell in enumerate(rows):
        if (
            (cell == "#")
            and x != 0
            and y != 0
            and x != (len(rows) - 1)
            and y != (len(cells) - 1)
        ):

            if (
                cells[y + 1][x + 1] == "#"
                and cells[y - 1][x + 1] == "#"
                and cells[y + 1][x - 1] == "#"
                and cells[y - 1][x - 1] == "#"
            ):
                cnt = 1
                while cells[y + cnt][x + cnt] == "#":
                    # print(cnt)

                    cnt += 1
                    # print(y + cnt, x + cnt)
                    if (x + cnt > (len(rows) - 1)) or (y + cnt > (len(cells) - 1)):
                        # 帳尻
                        break
                    if (x + cnt == (len(rows) - 1)) or (y + cnt == (len(cells) - 1)):
                        if cells[y + cnt][x + cnt] == "#":
                            cnt += 1
                        break

                # print(cnt)
                cnt -= 2
                ans[cnt] += 1

print(" ".join(list(map(str, ans))))

# 5 0 1 0 0 0 1 0 0 0 0 0 0 0 0
# 5 0 1 0 0 0 1 0 0 0 0 0 0 0 0
