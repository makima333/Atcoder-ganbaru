import io
from operator import mod
import sys

_INPUT = """\
1
1000000000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
n_lis = list(map(int, input().split()))

print(n_lis.index(max(n_lis)) + 1)
