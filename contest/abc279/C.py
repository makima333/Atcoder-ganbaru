import io
from operator import mod
import sys

_INPUT = """\
8 7
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
....###
####...
....###
####...
....###
####...
....###
####...

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())

s_grid = [[] for _ in range(w)]
for i in range(h):
    s_line = list(input())
    for j, s in enumerate(s_line):
        if s == "#":
            s_grid[j].append(str(i))


t_grid = [[] for _ in range(w)]
for i in range(h):
    t_line = list(input())
    for j, t in enumerate(t_line):
        if t == "#":
            t_grid[j].append(str(i))

t_cnt = {}
for t_col in t_grid:
    tmp_join = ",".join(t_col)
    if tmp_join in t_cnt.keys():
        t_cnt[tmp_join] += 1
    else:
        t_cnt[tmp_join] = 1


for s_col in s_grid:
    s_tmp_join = ",".join(s_col)
    if s_tmp_join in t_cnt.keys():
        if t_cnt[s_tmp_join] > 0:
            t_cnt[s_tmp_join] -= 1
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()
print("Yes")
