import io
from operator import mod
import sys

_INPUT = """\
4
2 5 7 8
5
2 9 10 11 19
20


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))
B_set = set(B)

x = int(input())

i = 0
current_step = 0
dp = [1]
dp += [0] * (x)

for current_step in range(x + 1):
    if dp[current_step] == 0:
        continue

    for a in A:
        if a + current_step == x:
            print("Yes")
            exit()
        if a + current_step not in B_set:
            if a + current_step < x:
                dp[a + current_step] = 1

print("No")
