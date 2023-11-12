import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
AAABCABCABCAABCABCBBBAABCBCCCAAABCBCBCC



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


S = input()
ans = S[:2]
S = S[2:]

for s in S:
    # print(ans)
    if len(ans) < 2:
        ans += s
        continue

    tmp = ans[-2] + ans[-1] + s

    if tmp == "ABC":
        ans = ans[:-2]
    else:
        ans += s

print("".join(ans))
