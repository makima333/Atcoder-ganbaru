import io
import sys

_INPUT = """\
4
ABBA
"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
# 文字数が奇数であること
# BBA → BAB
# ABBAA → ABABA 可能
# ABBBB → AABAB 無理
# BAAAA → BABAB 可能
n = int(input())
word = input()
res = 'No'

if str(word) == str(word)[::-1]:
    res = 'Yes'
elif n == 2:
    res = 'No'
elif (word[0] == 'A' and word[-1] == 'A') or \
         (word[0] == 'B'):
        res = 'Yes'
elif (word[0] == 'A' and word[-1] == 'A') or \
         (word[0] == 'B'):
        res = 'Yes'

print(res)
