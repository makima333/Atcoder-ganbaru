import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
Capitalized


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = input()

big_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_abc = "abcdefghijklmnopqrstuvwxyz"


if S[0] in big_abc:
    for s in list(S[1:]):
        if s in big_abc:
            print("No")
            exit()

    print("Yes")
else:
    print("No")
