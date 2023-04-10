import io
from operator import mod
import sys

_INPUT = """\
3 8



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

if a == b:
    print(0)
    exit()

cnt = 0


def cal(x, y):
    cnt = x % y
    res_num = x // y

    return (cnt, res_num)


while a != b:
    if a > b:
        cnt_tmp, num_tmp = cal(a, b)
        cnt += cnt_tmp
        a = num_tmp
    else:
        cnt_tmp, num_tmp = cal(b, a)
        cnt += cnt_tmp
        b = num_tmp
