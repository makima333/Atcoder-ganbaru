import io
from operator import mod
import sys

_INPUT = """\
10
9 8 6 5 10 3 1 2 4 7


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ps = list(map(int, input().split()))

ps.reverse()
tmp = []
for i, p in enumerate(ps):
    if tmp:
        if p < tmp[-1]:
            tmp.append(p)
        else:
            # tmp.append(p)
            break
    else:
        tmp.append(p)

tmp.sort()
import bisect

# print(tmp)
pop_i = bisect.bisect(tmp, p)
# print(ps)
# print(tmp[pop_i])
ps[i] = tmp.pop(pop_i - 1)

ps.reverse()
tmp.append(p)
tmp.sort()
tmp.reverse()


print(" ".join(list(map(str, ps[: len(ps) - i] + tmp))))
