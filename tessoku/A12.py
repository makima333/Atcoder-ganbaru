import io
from operator import mod
import sys

_INPUT = """\
4 10
1 2 3 4


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n, k = map(int, input().split())

aa = list(map(int, input().split()))
