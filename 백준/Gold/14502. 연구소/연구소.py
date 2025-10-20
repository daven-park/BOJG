import sys
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

virus = []

selected = set()
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))

def bfs(board):
    global answer
    visited = [[False] * M for _ in range(N)]
    new_board = deepcopy(board)

    q = deque(virus)
    for x, y in virus:
        visited[x][y] = True

    while q:
        curX, curY = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if new_board[nx][ny] != 0: continue
            if visited[nx][ny]: continue
            q.append((nx, ny))
            new_board[nx][ny] = 2
            visited[nx][ny] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

def dfs(start, cnt):
    if cnt == 3:
        for i in selected:
            if board[i // M][i % M] != 0:
                return
        for i in selected:
            board[i // M][i % M] = 1
        bfs(board)
        for i in selected:
            board[i // M][i % M] = 0
        return
    if (N * M - start) < (3 - cnt): return

    for i in range(start, N * M):
        if board[i // M][i % M] != 0: continue
        selected.add(i)
        dfs(i + 1, cnt + 1)
        selected.remove(i)

dfs(0, 0)
print(answer)