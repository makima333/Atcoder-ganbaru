import io
from operator import mod
import sys

_INPUT = """\
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
ans = {}
for _ in range(m):
    k, v = map(int, input().split())
    if k in ans.keys():
        ans[k].append(v)
    else:
        ans[k] = [v]

    if v in ans.keys():
        ans[v].append(k)
    else:
        ans[v] = [k]


for i in range(1, n + 1):
    if i in ans.keys():
        ans[i].sort()
        tmp_ans = " ".join(list(map(str, ans[i])))
        print(f"{len(ans[i])} {tmp_ans}")
    else:
        print(0)
