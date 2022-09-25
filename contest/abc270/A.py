import io
from operator import mod
import sys

_INPUT = """\
0 0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

ans = {0: [0], 1: [1], 2: [2], 4: [4], 3: [1, 2], 5: [1, 4], 6: [2, 4], 7: [1, 2, 4]}

c = 0
c_lis = []


c_lis += ans[a] + ans[b]
print(sum(set(c_lis)))
