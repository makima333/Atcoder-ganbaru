import io
import sys

_INPUT = """\
50 4 8
"""
sys.stdin = io.StringIO(_INPUT)
# 不正解でした
#---------------------------------
tmp = input()
N = int(tmp.split(" ")[0])
A = int(tmp.split(" ")[1])
B = int(tmp.split(" ")[2])

a_win = 0
for i in range(N):
    n = i + 1
    while True:
        # aliceのたーん
        if n >= A:
            nko = n // A
            n -= A*nko
        else:
            break

        # bobのたーん
        if n >= B:
            nko = n // B
            n -= B*nko
        else:
            a_win += 1
            break
print(a_win)