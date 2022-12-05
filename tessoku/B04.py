import io
from operator import mod
import sys

_INPUT = """\
1101


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
print(int(input(), 2))
