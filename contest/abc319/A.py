import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
tourist

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = input()
rank = {
    "tourist": 3858,
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481,
}

print(rank[S])
