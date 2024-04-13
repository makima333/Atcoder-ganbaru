import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
la
LAX


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


def check_airport_code(S, T):
    if T[-1] == "X":
        T = T[:2].lower()
    else:
        T = T.lower()

    last_index = -1
    for char in T:
        new_index = S.find(char, last_index + 1)
        if new_index == -1:
            return "No"
        last_index = new_index

    return "Yes"


# 入力
S = input()
T = input()

# 処理と出力
result = check_airport_code(S, T)
print(result)
