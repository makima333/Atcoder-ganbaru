import io
from operator import mod
import sys

_INPUT = """\
3 2 7
2 7 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, x, y = map(int, input().split())
A = list(map(int, input().split()))

# p2 point
xset = set([A[0]])
yset = set([0])


# x座標 (偶数)
for i in range(2, n, 2):
    tmp_a = A[i]
    tmp_set = set()
    for j in xset:
        tmp_set.add(j + tmp_a)
        tmp_set.add(j - tmp_a)
    xset = tmp_set

# y座標 (奇数)
for i in range(1, n, 2):
    tmp_a = A[i]
    tmp_set = set()
    for j in yset:
        tmp_set.add(j + tmp_a)
        tmp_set.add(j - tmp_a)
    yset = tmp_set

ans = "Yes" if (x in xset) and (y in yset) else "No"
print(ans)
