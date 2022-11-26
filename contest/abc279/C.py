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

s_grid = [set([]) for _ in range(w)]
s_cnt = [{"index": i, "cnt": 0} for i in range(w)]
for i in range(h):
    s_line = list(input())
    for j, s in enumerate(s_line):
        if s == "#":
            s_grid[j].add(i)
            s_cnt[j]["cnt"] += 1

# print(s_grid)
s_cnt.sort(key=lambda x: x["cnt"], reverse=True)
# print(s_cnt)

t_grid = [set([]) for _ in range(w)]
t_cnt = [{"index": i, "cnt": 0} for i in range(w)]
for i in range(h):
    t_line = list(input())
    for j, t in enumerate(t_line):
        if t == "#":
            t_grid[j].add(i)
            t_cnt[j]["cnt"] += 1

t_cnt.sort(key=lambda x: x["cnt"], reverse=True)

for s_dict in s_cnt:
    s_row = s_grid[s_dict["index"]]
    s_row_len = len(s_row)
    for t_k, t_dict in enumerate(t_cnt):
        tmp_index = t_dict["index"]
        tmp_len = t_dict["cnt"]
        if tmp_len != s_row_len:
            print("No")
            exit()
        if (s_row - t_grid[tmp_index]) == set([]):
            # t_grid.pop(tmp_index)
            break
    t_cnt.pop(t_k)
print("Yes")
