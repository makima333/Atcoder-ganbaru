import io
from operator import mod
import sys

_INPUT = """\
4 10
1
1
3
2 1
1
2 3
3
1
2 2
3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, q = map(int, input().split())

not_come = set()
not_call = list(range(n, 0, -1))

come_history = set()

for _ in range(q):
    event = input()

    if event.count(" ") == 0:
        event = int(event)
        if event == 1:
            tmp = not_call.pop()
            not_come.add(tmp)
        elif event == 3:
            # not_come -= come_history

            for ans in not_come:
                print(ans)
                break

    else:
        event, person = map(int, event.split())
        come_history.add(person)
        not_come.discard(person)
