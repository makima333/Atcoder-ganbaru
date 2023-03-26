import io
from operator import mod
import sys

_INPUT = """\
4 6
#.#3#.
###.#.
##.###
#1..#.


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = input()
cc = input().split()

words = set(["and", "not", "that", "the", "you"])

for c in cc:
    # print(c)
    if c in words:
        print("Yes")
        exit()
print("No")
