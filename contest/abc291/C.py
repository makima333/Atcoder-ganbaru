import io
from operator import mod
import sys

_INPUT = """\
20
URDDLLUUURRRDDDDLLLL



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = list(input())

history = set([(0, 0)])
pos = [0, 0]

for s in ss:
    if s == "R":
        pos[0] += 1
    if s == "L":
        pos[0] -= 1
    if s == "U":
        pos[1] += 1
    if s == "D":
        pos[1] -= 1

    if (pos[0], pos[1]) in history:
        print("Yes")
        exit()
    else:
        history.add((pos[0], pos[1]))

print("No")
