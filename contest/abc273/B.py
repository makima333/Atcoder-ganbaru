import io
from operator import mod
import sys

_INPUT = """\
499 3

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

nums = list(str(a))
nums.reverse()

if b > len(nums):
    print(0)
    exit()

res = [0] * (b + 1)
for i in range(b):
    if int(nums[i]) + res[i] >= 5:
        res[i + 1] += 1

nums.reverse()

ans = 0
if b == len(nums):
    # ans = int("".join(nums[0]))
    if res[-1]:
        ans = 0
    else:
        print(0)
        exit()

else:
    ans = int("".join(nums[:-b]))

zero = "".join(["0"] * b)
if res[-1]:
    ans += 1

print(f"{ans}{zero}")
