import io
from operator import mod
import sys

_INPUT = """\
3 5
#.#..
.....
.#...
2 2
#.
.#
5 3
...
#.#
.#.
.#.
...


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
# マス
def convert(h, w, g):
    s = set()
    for i in range(h):
        for j in range(w):
            if g[i][j] == "#":
                s.add((i, j))

    return s


def normalize(s):
    min_y = min(y for (y, x) in s)
    min_x = min(x for (y, x) in s)
    return set((y - min_y, x - min_x) for (y, x) in s)


a_h, a_w = map(int, input().split())
aa_set = normalize(convert(a_h, a_w, [input() for _ in range(a_h)]))

b_h, b_w = map(int, input().split())
bb_set = normalize(convert(b_h, b_w, [input() for _ in range(b_h)]))

x_h, x_w = map(int, input().split())
xx_set = normalize(convert(x_h, x_w, [input() for _ in range(x_h)]))


ans = False
for dy in range(-x_h, x_h):
    for dx in range(-x_w, x_w):
        ans |= normalize(aa_set.union((y + dy, x + dx) for (y, x) in bb_set)) == xx_set

print("Yes" if ans else "No")
