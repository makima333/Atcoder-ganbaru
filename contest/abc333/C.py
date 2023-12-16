import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
333

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

repnits = []
o = "1"

for _ in range(12):
    repnits.append(int(o))
    o += "1"

anses = set()
for i in range(12):
    for j in range(12):
        for k in range(12):
            anses.add(repnits[i] + repnits[j] + repnits[k])

anses = list(anses)

anses.sort()
print(anses[int(input()) - 1])
