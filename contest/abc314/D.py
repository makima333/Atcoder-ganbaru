import io
from operator import mod
import sys

_INPUT = """\
35
TheQuickBrownFoxJumpsOverTheLazyDog
10
2 0 a
1 19 G
1 13 m
1 2 E
1 21 F
2 0 a
1 27 b
3 0 a
3 0 a
1 15 i


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
S = input()

ans = list(S)
ans_time = [-1 for _ in range(N)]
last_q = -1
last_type = ""

Q = int(input())
for q in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)

    if t == 1:
        ans[x - 1] = c
        ans_time[x - 1] = q
    else:
        if t == 2:
            last_q, last_type = (q, "lower")
        elif t == 3:
            last_q, last_type = (q, "upper")


if last_q == -1:
    print("".join(ans))
    exit()


def conv_ul(convstr, ul):
    if ul == "upper":
        return convstr.upper()
    else:
        return convstr.lower()


for i, q_k in enumerate(ans_time):
    if last_q > q_k:
        ans[i] = conv_ul(ans[i], last_type)


print("".join(ans))
