import io
from operator import mod
import sys

_INPUT = """\
4
15 5 2 10

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
s = input()
ss = list(map(int, input().split()))
ans = max(ss) - ss[0]

if len(ss) > 1:
    ss_ex = ss[1:]
    if max(ss_ex) >= ss[0]:
        ans += 1

print(ans)
