import io
import sys

_INPUT = """\
4 4
"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
L, R= map(int, input().split())

atcoder = "atcoder"

print(atcoder[L-1:R])

