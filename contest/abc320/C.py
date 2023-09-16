import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
123
314
512


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


from itertools import permutations

M = int(input())
ss = []
for _ in range(3):
    ss.append(list(map(int, list(input()))))

common_numbers = set(ss[0]) & set(ss[1]) & set(ss[2])

if len(common_numbers) == 0:
    print(-1)
    exit()


def solve(p, d):
    if any(d not in ss[i] for i in range(3)):
        return 10**9

    crr = 0
    for i in range(3):
        if ss[p[i]][crr % M :].count(d) == 0:
            ss[p[i]] += ss[p[i]]

        crr += ss[p[i]][crr % M :].index(d) + 1
    return crr - 1


ans = 10**9
for d in range(10):
    for p in permutations(range(3)):
        ans = min(ans, solve(p, d))
print(ans)
