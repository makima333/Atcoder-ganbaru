import io
from operator import mod
import sys

_INPUT = """\
8 6 1
2 5 6 5 2 1 7 9
7 2 5 5 2 4


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import bisect

n, m, d = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

aa.sort()
ans = -1

# print(aa)
for b in bb:
    a = aa[bisect.bisect_left(aa, b + d) - 1]
    if abs(a - b) <= d:
        ans = max(ans, a + b)

    try:
        a = aa[bisect.bisect_left(aa, b + d)]
        if abs(a - b) <= d:
            ans = max(ans, a + b)
    except:
        pass

print(ans)
