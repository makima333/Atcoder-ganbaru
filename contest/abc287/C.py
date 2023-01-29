import io
from operator import mod
import sys

_INPUT = """\
4 3
1 3
4 2
3 2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

n, m = map(int, input().split())

vec = [0]
vec += [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    vec[u].append(v)
    vec[v].append(u)

start_end = []

for ve_i, ve in enumerate(vec):
    if ve == 0:
        continue

    if len(ve) > 2:
        print("No")
        exit()
    elif len(ve) == 1:
        start_end.append(ve_i)
    elif len(ve) == 0:
        print("No")
        exit()
    else:
        continue

if len(start_end) == 0:
    print("No")
    exit()

if len(start_end) != 2:
    print("No")
    exit()


current_ve = start_end[0]
before_ve = 0
his = set([])
while True:
    # print(current_ve)
    his.add(current_ve)
    ve = vec[current_ve]
    if current_ve != start_end[0] and len(ve) == 1:
        if len(his) == n:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    if ve[0] == before_ve:
        before_ve = current_ve
        current_ve = ve[1]
    else:
        before_ve = current_ve
        current_ve = ve[0]
