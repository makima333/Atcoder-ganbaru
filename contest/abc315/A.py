import io
from operator import mod
import sys

_INPUT = """\
atcodera


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

ss = input()

ss = ss.replace("a", "")
ss = ss.replace("i", "")
ss = ss.replace("u", "")
ss = ss.replace("e", "")
ss = ss.replace("o", "")

print(ss)
