import io
import sys
from tokenize import Double

_INPUT = """\
100 1 1000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

x, y, z = map(int, input().split())


def sim(init, dir, x, y, z, hanma) -> int:
    current = init
    cost = 0
    while True:
        next = current + dir
        cost += 1
        if next == 1001 or next == -1001:
            return -1

        if x == next:
            return cost

        if y == next:
            if hanma == 0:
                return -1
            if hanma == 1:
                pass
        if z == next:
            z_p = sim(next, 1, x, y, z, 1)
            z_m = sim(next, -1, x, y, z, 1)
            if min(z_p, z_m) == -1:
                return cost + max(z_p, z_m)
            else:
                return min(z_p, z_m)

        current = next


ans_p = sim(0, 1, x, y, z, 0)
ans_m = sim(0, -1, x, y, z, 0)
if min(ans_p, ans_m) == -1:
    ans = max(ans_p, ans_m)
else:
    ans = min(ans_p, ans_m)

print(ans)
