import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
abracadabra


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
S = input()
ans = set()

for i in range(len(S) - 1):
    tmp_S = S[i:]
    for j in range(len(tmp_S)):
        s = tmp_S[: len(tmp_S) - j]
        # print(s)
        ans.add(s)

ans.add(S[-1])

# print(ans)
print(len(ans))
