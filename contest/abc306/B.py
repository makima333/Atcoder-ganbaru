import io
from operator import mod
import sys

_INPUT = """\
1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
aa = input().split()

ans = 0
for a_i, a in enumerate(aa):
    tmp_a = int(a)

    ans += tmp_a * (2**a_i)

print(ans)
