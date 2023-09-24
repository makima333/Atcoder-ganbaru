import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
7 12 25514963
2436426 24979445 61648772 23690081 33933447 76190629 62703497
11047202 71407775 28894325 31963982 22804784 50968417 30302156 82631932 61735902 80895728 23078537 7723857


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

n, m, p = map(int, input().split())

main = list(map(int, input().split()))
sub = list(map(int, input().split()))

sub.sort()
sub_sum = [0]
for dish in sub:
    sub_sum.append(sub_sum[-1] + dish)

sub_sum = sub_sum[1:]

ans = 0
import bisect

for main_d in main:
    target = p - main_d
    if target > sub[-1]:
        ans += sub_sum[-1] + (m * main_d)
    elif target > sub[0]:
        idx = bisect.bisect(sub, target)
        ans += sub_sum[idx - 1] + (idx * main_d) + (p * (m - idx))

    else:
        ans += p * m


print(ans)
