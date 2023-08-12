import io
from operator import mod
import sys

_INPUT = """\
3
1
1
1
2
1
3
0


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
bet = []

for _ in range(N):
    c = int(input())
    aa = set(list(map(int, input().split())))
    bet.append((c, aa))

X = int(input())
ans_can = [100 for _ in range(N)]
for b_i, b in enumerate(bet):
    c, aa = b
    if X in aa:
        ans_can[b_i] = c

minc = min(ans_can)
if minc == 100:
    print(0)
    # print()
    exit()

ans = []

for i, answer in enumerate(ans_can):
    if minc == answer:
        ans.append(i + 1)


print(len(ans))
print(*ans)
