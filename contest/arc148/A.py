import io
import sys

_INPUT = """\
10
3785 5176 10740 7744 3999 3143 9028 2822 4748 6888

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
import math
n = int(input())
nums = list(map(int, input().split()))

if len(set(nums)) == 1:
    print("1")
    exit()

tmp = 0
for i, num in enumerate(nums):
    if i+1 == len(nums):
        break
    tmp = math.gcd(tmp, abs(nums[i] - nums[i + 1]))
    print(tmp, )


print("2" if tmp == 1 else 1)
        

        
