import io
from operator import mod
import sys

_INPUT = """\
99

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

if n % 5 >= 3:
    ans = n + (5 - (n % 5))
else:
    ans = n - (n % 5)

print(ans)
