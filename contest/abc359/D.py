import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
7 4
AB?A?BA

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, K = map(int, input().split())

S = input()
mp = {"C" * (K - 1): 1}


for c in S:
    tmp = (
        {s + "A": v for s, v in mp.items()}
        if c != "B"
        else {} | {s + "B": v for s, v in mp.items()} if c != "A" else {}
    )

    mp = {}

    for s, v in tmp.items():
        if s != s[::-1]:
            if s[1:] in mp:
                mp[s[1:]] += v
            else:
                mp[s[1:]] = v


print(mp)
