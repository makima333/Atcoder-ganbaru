import io
from operator import mod
import sys

_INPUT = """\
6
1 2 4 6 7 271 8 5 5 5


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
vols = list(map(int, input().split()))
v_arr = set(vols)

v_cnt = len(v_arr)

# 重複巻数
sell_cnt = len(vols) - len(v_arr)

sell_able_cnt = v_cnt + sell_cnt

v_arr = list(v_arr)
v_arr.sort()

cnt = 1
sold_cnt = 0

while True:

    try:
        tmp_vol = v_arr[(cnt - 1) - sold_cnt]
    except IndexError:
        if sell_able_cnt > 1:
            sell_able_cnt -= 2
            cnt += 1
            sold_cnt += 1
        else:
            break
    else:
        if tmp_vol == cnt and sell_able_cnt > 0:
            cnt += 1
            v_cnt -= 1
            sell_able_cnt -= 1
        else:
            if sell_able_cnt > 1:
                sell_able_cnt -= 2
                cnt += 1
                sold_cnt += 1
            else:
                break


print(cnt - 1)
