import sys
from collections import deque, defaultdict

input = sys.stdin.readline

S = int(input())
visited = set()
q = deque()
q.append((1, 0, 0))
visited.add((1, 0))
while q:
    display, clipboard, time = q.popleft()
    if display == S:
        print(time)
        break
    for op in ["C", "P", "D"]:
        if op == "C":
            nc = display
            if (display, nc) in visited: continue
            q.append((display, nc, time + 1))
            visited.add((display, nc))
        elif op == "P":
            nd = display + clipboard
            if (nd, clipboard) in visited: continue
            q.append((nd, clipboard, time + 1))
            visited.add((nd, clipboard))
        else:
            nd = display - 1
            if (nd, clipboard) in visited: continue
            q.append((nd, clipboard, time + 1))
            visited.add((nd, clipboard))