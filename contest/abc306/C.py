import io
from operator import mod
import sys

_INPUT = """\
3
1 1 3 2 3 2 2 3 1

......


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

n = int(input())
aa = list(map(int, input().split()))

index = [[i, 0] for i in range(n + 1)]
history = set([])

for ai, a in enumerate(aa):
    if index[a][1] == 0:
        index[a][1] = ai + 1
    elif index[a][1] != 0:
        if a not in history:
            index[a][1] = ai + 1
            history.add(a)

index.pop(0)
for ans in sorted(index, key=lambda x: x[1]):
    # if ans[0] != 0:
    print(ans[0], end=" ")
