import io
from operator import mod
import sys

_INPUT = """\
1 1
4 128 741 239 901
1 1

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

n_arrs = [list(map(int, input().split())) for _ in range(a)]
q_arrs = [list(map(int, input().split())) for _ in range(b)]


for q in q_arrs:
    arr_i = q[0]
    elm_i = q[1]

    print(n_arrs[arr_i - 1][elm_i])
