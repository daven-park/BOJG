import sys
from collections import deque

N, M = map(int, input().split())
board = [[ch for ch in input()] for _ in range(N)]

start = None
for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            start = (i, j)


def bfs(x, y):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    q.append((x, y))
    visited[x][y] = True
    ret = 0
    while q:
        curX, curY = q.popleft()
        if board[curX][curY] == 'P':
            ret += 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 'X' : continue
            q.append((nx, ny))
            visited[nx][ny] = True

    return ret

answer = bfs(start[0], start[1])
print("TT" if answer == 0 else answer)