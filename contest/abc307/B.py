import io
from operator import mod
import sys

_INPUT = """\
5
ab
ccef
da
a
fe


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

ss = [input() for _ in range(n)]

# 回文
# a,b: string
# retrun : boolean
def kaibun(a, b):
    c = a + b
    lenc = len(c)
    if lenc % 2 == 0:
        # print(c[: (lenc // 2)], c[lenc // 2 :][::-1])
        if c[: (lenc // 2)] == c[lenc // 2 :][::-1]:
            return True
        else:
            return False
    else:
        if c[: (lenc // 2)] == c[(lenc // 2) + 1 :][::-1]:
            return True
        else:
            return False


for s_i, s in enumerate(ss):
    for k_j, k in enumerate(ss):
        if s_i != k_j:
            if kaibun(s, k):
                print("Yes")
                exit()

print("No")
