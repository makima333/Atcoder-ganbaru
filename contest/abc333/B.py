import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
AC
EC


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

group_short = set(
    [
        "AB",
        "BA",
        "BC",
        "CB",
        "CD",
        "DC",
        "DE",
        "ED",
        "EA",
        "AE",
    ]
)


S = input()
T = input()

if S in group_short and T in group_short:
    print("Yes")
elif S not in group_short and T not in group_short:
    print("Yes")
else:
    print("No")
