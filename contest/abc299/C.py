import io
from operator import mod
import sys

_INPUT = """\
30
-o-o-oooo-oo-o-ooooooo--oooo-o


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = input()

dango = input()

if "-" not in dango:
    print(-1)
    exit()

while "--" in dango:
    dango = dango.replace("--", "-")

# print(dango)
max_x = -1
for d in dango.split("-"):
    max_x = max(max_x, len(d))


print(max_x if max_x != 0 else -1)
