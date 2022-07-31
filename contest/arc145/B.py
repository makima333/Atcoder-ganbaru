import io
import sys

_INPUT = """\
4 2 1

"""
sys.stdin = io.StringIO(_INPUT)
#---------------------------------
tmp = input()
N = int(tmp.split(" ")[0])
A = int(tmp.split(" ")[1])
B = int(tmp.split(" ")[2])

a_win = 0
laund = N-(A-1)

if A <= B:
    a_win = laund
elif laund != 0:
    # Aの勝利条件
    # n mod A < B
    # 10 4 3 のとき
    # n = 1,2,3,4,5,6,7,8,9,10
    # n mod A = 1,2,3,0,1,2,3,0,1,2
    # n mod A < B = 1,2,0,1,2,0,1,2
    # mod の周期数 0,1,2,3部分のうち勝てるのはB個

    a_win = (laund//A) * B + min(laund%A, B)


print(max(a_win,0))
