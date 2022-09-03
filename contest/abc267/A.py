import io
from operator import mod
import sys

_INPUT = """\
Wednesday



"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
in_str = input()
dict = {"Monday":5, "Tuesday":4, "Wednesday":3, "Thursday":2, "Friday":1}
print(dict[in_str])