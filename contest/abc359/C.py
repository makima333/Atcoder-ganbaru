import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 0
-1 0


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())


Sx -= 1 if (Sx + Sy) % 2 == 1 else 0
Tx -= 1 if (Tx + Ty) % 2 == 1 else 0


dx = abs(Sx - Tx)
dy = abs(Sy - Ty)

print((dy + max(dy, dx)) // 2)
