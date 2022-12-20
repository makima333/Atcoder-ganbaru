import io
import sys

_INPUT = """\
12 12 11 1 2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
A, B, C, D, E = map(int, input().split())

nums = set([A, B, C, D, E])
if len(nums) != 2:
    print("No")
    exit()

for n in nums:
    cnt = len([0 for m in [A, B, C, D, E] if m == n])
    if cnt == 2 or cnt == 3:
        print("Yes")
        exit()

print("No")
