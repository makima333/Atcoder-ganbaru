import io
from operator import mod
import sys

_INPUT = """\
20 40



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ab, cd = map(str, input().split())


while True:

    ab = ab.zfill(2)
    cd = cd.zfill(2)
    a = ab[0]
    b = ab[1]
    c = cd[0]
    d = cd[1]

    # swap
    c, b = b, c

    ab_num = int(f"{a}{b}")
    cd_num = int(f"{c}{d}")

    if ab_num < 24 and cd_num < 59:
        # reswap
        c, b = b, c

        ab_num = int(f"{a}{b}")
        cd_num = int(f"{c}{d}")

        print(f"{ab_num} {cd_num}")
        break

    # reswap
    c, b = b, c

    ab_num = int(f"{a}{b}")
    cd_num = int(f"{c}{d}")

    # print(f"{ab_num} {cd_num}")
    cd = str((cd_num + 1) % 60)
    if cd == "0":
        ab = str((ab_num + 1) % 24)
