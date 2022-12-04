import io
from operator import mod
import sys

_INPUT = """\
10
314159265 358979323 846264338 -327950288 419716939 -937510582 97494459 230781640 628620899 -862803482

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = list(map(int, input().split()))

ans = [ss[0]]
tmp = 0
ss = ss[1:]

for s in ss:
    tmp = sum(ans)
    ans.append(s - tmp)

print(*ans)
