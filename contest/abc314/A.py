import io
from operator import mod
import sys

_INPUT = """\
1


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
print(pi[: int(input()) + 2])
