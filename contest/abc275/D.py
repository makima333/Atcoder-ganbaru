import io
from operator import mod
import sys

_INPUT = """\
100

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
# メモ化再帰
# 検索用：メモ,メモ再帰
from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(int(input())))
