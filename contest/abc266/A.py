import io
from operator import mod
import sys

_INPUT = """\
a


"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
in_str = input()

print(in_str[len(list(in_str)) // 2])