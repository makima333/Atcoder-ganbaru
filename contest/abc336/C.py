import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

if N == 1:
    print(0)
    exit()

n = N - 1
a = ""

while n > 0:
    m = n % 5
    m = str(m)

    a = f"{m}{a}"
    n = n // 5

five = ["0", "2", "4", "6", "8"]


ans = ""
for s in list(str(int(a))):
    ans = f"{ans}{five[int(s)]}"

print(ans)
