import io
from operator import mod
import sys

_INPUT = """\
8 1000000000 1000000000
bcdfcgaa


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

n, a, b = map(int, input().split())
ss = list(input())
ans = []

import copy

tmp = 0
if n % 2 == 0:
    tmp = 1

for i in range(int(n / 2) + tmp):
    tmp_ans = 0
    tmp_ans += a * i

    if i != 0:
        tmp_ss = copy.copy(ss[i:])
        tmp_ss += copy.copy(ss[0:i])
    else:
        tmp_ss = copy.copy(ss)

    for j in range(int(n / 2)):
        if tmp_ss[j] != tmp_ss[len(tmp_ss) - j - 1]:
            tmp_ans += b

    ans.append(tmp_ans)


print(min(ans))
