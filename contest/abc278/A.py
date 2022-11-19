import io
from operator import mod
import sys

_INPUT = """\
9 5
1 2 3 4 5 6 7 8 9



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())
ns = list(map(int, input().split()))
# ns.reverse()
for i in range(k):
    ns.append(0)
print(*ns[k:])
