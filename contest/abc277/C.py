import io
from operator import mod
import sys

_INPUT = """\
6
1 3
1 5
1 12
3 5
3 12
5 12

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

# key : step, value: dist of set()
hashigo = {}

for _ in range(n):
    a, b = map(int, input().split())

    if a in hashigo.keys():
        hashigo[a].add(b)
    else:
        hashigo[a] = set([b])

    if b in hashigo.keys():
        hashigo[b].add(a)
    else:
        hashigo[b] = set([a])

if 1 not in hashigo.keys():
    print(1)
    exit()

step = 1
history = set([])
next = set([1])
while True:
    new_next = set([])

    for i in next:
        history.add(i)
        tmp_set = hashigo[i] - history
        for j in tmp_set:
            new_next.add(j)

    if len(new_next) == 0:
        break

    next = new_next

print(max(history))
