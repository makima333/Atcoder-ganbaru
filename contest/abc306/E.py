import io
from operator import mod
import sys

_INPUT = """\
4 2 10
1 5
2 1
3 3
4 2
2 10
1 0
4 0
3 1
2 0
3 0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import heapq


def solve(N, Q, K, queries):
    # AとBを初期化
    A = [0] * N
    B = [0] * K

    # heapqは最小ヒープなので、最大ヒープを実現するためには数を負にする
    heapq.heapify(B)

    for i in range(Q):
        Xi, Yi = queries[i]
        Xi -= 1  # 0-indexedにする

        # A[Xi]がBの中にあれば削除
        if A[Xi] in B:
            B.remove(A[Xi])
            heapq.heapify(B)

        # A[Xi]を更新
        A[Xi] = Yi

        # Bの最小値より大きいなら、Bの最小値を削除し、Yiを挿入
        if Yi > B[0]:
            heapq.heappop(B)
            heapq.heappush(B, Yi)

        # Bの全要素の和を出力
        print(sum(B))


N, Q, K = map(int, input().split())

queries = [(3, 10), (1, 20), (4, 30), (1, 40)]
solve(N, Q, K, queries)
