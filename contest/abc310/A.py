import io
from operator import mod
import sys

_INPUT = """\
3 100 50
60000 20000 40000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, p, q = map(int, input().split())

ans = 10**9

for d in list(map(int, input().split())):
    ans = min(ans, d+q)

print(min(ans, p))