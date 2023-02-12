import io
from operator import mod
import sys

_INPUT = """\
1 4
000111
000
111
999
111


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())


ss = ["".join(list(input())[-3:]) for _ in range(n)]
tt = [input() for _ in range(m)]

ans = 0
for s in ss:
    for t in tt:
        # print(s, t)
        if s == t:
            ans += 1
            break

print(ans)
