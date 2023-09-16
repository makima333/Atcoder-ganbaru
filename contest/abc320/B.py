import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
DEBABHOGE



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


def kaibun(c):
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


S = input()
ss = list(S)
ans = 0
import copy

for s_i in range(len(ss)):
    tmp_ss = copy.copy(ss[s_i:])
    tmp_s = "".join(tmp_ss)

    while True:
        if kaibun(tmp_s):
            # print(tmp_s)
            # print(ans, len(tmp_s))
            ans = max(ans, len(tmp_s))
            break

        tmp_s = tmp_s[:-1]
        if tmp_s == "":
            break


print(ans)
