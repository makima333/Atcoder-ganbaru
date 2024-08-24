import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4
1 1 1 

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
H = list(map(int, input().split()))

current_time = 0

for hp in H:
    while current_time % 3 != 0 and hp > 0:
        current_time += 1
        if current_time % 3 == 0:
            hp -= 3
        else:
            hp -= 1

    if hp <= 0:
        continue

    num = hp // 5
    current_time += num * 3
    hp -= num * 5

    while hp > 0:
        current_time += 1
        if current_time % 3 == 0:
            hp -= 3
        else:
            hp -= 1

print(current_time)
