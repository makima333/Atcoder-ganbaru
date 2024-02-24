import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
34
supercalifragilisticexpialidocious
20
g c
l g
g m
c m
r o
s e
a a
o f
f s
e t
t l
d v
p k
v h
x i
h n
n j
i r
s i
u a



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
S = input()
Q = int(input())

alphabet_dict = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z",
}

for _ in range(Q):
    a, b = map(str, input().split())
    if a == b:
        continue
    # alphabet_dict[a] = b
    for al in alphabet_dict:
        if alphabet_dict[al] == a:
            alphabet_dict[al] = b

ans = ""
for s in S:
    ans += alphabet_dict[s]


print(ans)
# print(alphabet_dict)
