import io
from operator import mod
import sys

_INPUT = """\
3 9
3 1
3 2
1 2
2 1
3 1
3 2
1 2
3 2
3 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, q = map(int, input().split())

ans = [0] + [0 for _ in range(n)]


for _ in range(q):
    e, p_i = map(int, input().split())
    # print(ans)
    if e == 1:
        ans[p_i] += 1
    if e == 2:
        ans[p_i] += 2
    if e == 3:
        if ans[p_i] > 1:
            print("Yes")
        else:
            print("No")
