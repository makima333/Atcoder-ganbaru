import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
32 101
65 78
2 29
46 55
103 130
52 40

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


def solve(n, cards):

    cards.sort(key=lambda x: -x[0])
    costs = []
    ans = []
    for a, c, i in cards:
        # print(a, c, i)

        if costs == []:
            costs.append(c)
            ans.append(i)
            continue
        else:
            if costs[-1] > c:
                costs.append(c)
                ans.append(i)

    ans.sort()
    return ans


n = int(input())
cards = []

for i in range(n):
    a, c = map(int, input().split())
    cards.append((a, c, i + 1))

result = solve(n, cards)

print(len(result))
print(*result)
