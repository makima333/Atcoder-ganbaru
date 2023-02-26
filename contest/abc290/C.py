import io
from operator import mod
import sys

_INPUT = """\
7 3
2 0 2 3 2 1 9


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())
aa = list(map(int, input().split()))
aa.sort()
aa = set(aa)

ans = 0
for a_i, a in enumerate(aa):
    if ans == a:
        k -= 1
        ans += 1
        if k == 0:
            break
    else:
        break

print(ans)
