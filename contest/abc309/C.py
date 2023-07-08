import io
from operator import mod
import sys

_INPUT = """\
15 158260522
877914575 2436426
24979445 61648772
623690081 33933447
476190629 62703497
211047202 71407775
628894325 31963982
822804784 50968417
430302156 82631932
161735902 80895728
923078537 7723857
189330739 10286918
802329211 4539679
303238506 17063340
492686568 73361868
125660016 50287940

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
# 2分探索、binary search

n, k = map(int, input().split())

aabb = []
for _ in range(n):
    a, b = map(int, input().split())
    aabb.append((a, b))


def logic(x):
    tmp = [ab[1] for ab in aabb if ab[0] >= x]
    return sum(tmp)


left = 1
right = 10**9 + 1
while left < right:
    mid = (left + right) // 2
    tmp_sum = logic(mid)

    if tmp_sum <= k:
        right = mid
    else:
        left = mid + 1

print(right)
