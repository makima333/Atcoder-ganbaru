import io
from operator import mod
import sys

_INPUT = """\
1597 987

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

if a == b:
    print(0)
    exit()

cnt = 0


def cal(x, y):
    res_num = x % y
    cnt = x // y

    if res_num != 0:
        return (cnt, res_num)
    else:
        return (cnt - 1, y)


while a != b:
    if a > b:
        cnt_tmp, num_tmp = cal(a, b)
        cnt += cnt_tmp
        a = num_tmp
    else:
        cnt_tmp, num_tmp = cal(b, a)
        cnt += cnt_tmp
        b = num_tmp


print(cnt)
