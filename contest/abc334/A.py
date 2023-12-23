import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
300 100

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
bat, groube = map(int, input().split())

if bat > groube:
    print("Bat")
else:
    print("Glove")
