import io
from operator import mod
import sys

_INPUT = """\
2
1000 2000 3000 4000 5000 6000 7000 2000 3000 4000 5000 6000 7000 8000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

aa = list(map(int, input().split()))

anss = []
ans = 0
for i in range(1, (n * 7) + 1):
    ans += aa[i - 1]
    if i % 7 == 0 and i != 0:
        # print("a")
        anss.append(ans)
        ans = 0


print(*anss)
