import io
from operator import mod
import sys

_INPUT = """\
8 4
fast
face
cast
race
fact
rice
nice
case

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
ss = set(list(input() for _ in range(n)))
import copy
from collections import defaultdict

tt = copy.copy(ss)
ans = defaultdict(list)

for s_i, s in enumerate(ss):
    tmp_arrs = tt - set([s])
    for arr in tmp_arrs:
        tmp_diif = 0
        for j in range(m):
            if list(s)[j] == list(arr)[j]:
                pass
            else:
                tmp_diif += 1

        if tmp_diif == 1:
            ans[s].append(arr)


visited = set([])


def dfs(node):
    visited.add(node)
    for t in ans[node]:
        if t not in visited:
            dfs(t)


if len(list(ans.keys())) != n:
    print("No")
    exit()

dfs(list(ans.keys())[0])
if set(ans.keys()) == visited:
    print("Yes")
else:
    print("No")
