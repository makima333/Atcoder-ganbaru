import io
from operator import mod
import sys

_INPUT = """\
4
3
1 2 3
2
20 23
10
6 10 4 1 5 9 8 6 5 1
1
1000000000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    for ai in list(map(int, input().split())):
        if ai % 2 == 1:
            ans += 1
    print(ans)
