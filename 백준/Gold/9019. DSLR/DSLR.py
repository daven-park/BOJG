import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def operations(idx, current):
    ret = 0
    cmd = ""
    # D
    if idx == 0:
        ret = current * 2 % 10000
        cmd += "D"
    # S
    elif idx == 1:
        ret = (current - 1) % 10000
        cmd += "S"
    # L
    elif idx == 2:
        ret = current // 1000 + (current % 1000) * 10
        cmd += "L"
    # R
    else:
        ret = current // 10 + (current % 10) * 1000
        cmd += "R"
    return ret, cmd

def bfs(a, b, visited):
    q = deque()
    q.append((a, ""))
    visited[a] = True
    while q:
        current, count = q.popleft()
        if current == b:
            return count
        for op in range(4):
            next_num, cmd = operations(op, current)
            if visited[next_num]: continue
            visited[next_num] = True
            q.append((next_num, count + cmd))

for _ in range(T):
    a, b = map(int, input().split())

    visited = [False] * 10001
    print(bfs(a, b, visited))