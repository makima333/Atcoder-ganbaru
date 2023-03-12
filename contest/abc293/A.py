import io
from operator import mod
import sys

_INPUT = """\
atcoderbeginnercontest



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ss = [0] + list(input())
# print(ss)
ans = [""] * (len(ss) + 1)

for i, s in enumerate(ss):

    if i == 0:
        continue

    if i % 2 == 1:
        ans[i] = s
    else:
        ans[i - 2] = s

print("".join(ans[:-2]))
