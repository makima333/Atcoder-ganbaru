import io
from operator import mod
import sys

_INPUT = """\
2 2
1 3
2 1


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())

cells = [list(map(int, input().split())) for _ in range(h)]


h_m1 = h - 1
w_m1 = w - 1

m = h_m1 + w_m1

bits = [0] * m
ans = 0
for i in range(2**m):
    comb = [int(j) for j in format(i, f"0{m}b")]

    if sum(comb) == h_m1:
        his = set([])
        h_i = 1
        w_i = 1
        for b in comb:
            v = cells[h_i - 1][w_i - 1]
            if v in his:
                break
            else:
                his.add(v)
                if b == 1:
                    h_i += 1
                else:
                    w_i += 1

        if h_i == h and w_i == w:
            if cells[h - 1][w - 1] not in his:
                ans += 1


print(ans)
