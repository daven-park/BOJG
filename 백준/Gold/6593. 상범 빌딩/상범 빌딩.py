import sys
from collections import deque

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0: break

    board = []

    for i in range(L):
        floor = [list(ch for ch in input().strip()) for _ in range(R)]
        input()
        board.append(floor)

    start, exit = None, None
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    start = (i, j, k)
                if board[i][j][k] == 'E':
                    exit = (i, j, k)

    answer = 0
    q = deque()
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    f, x, y = start
    q.append((f, x, y, 0))
    visited[f][x][y] = True
    while q:
        cf, cx, cy, cnt = q.popleft()
        if cf == exit[0] and cx == exit[1] and cy == exit[2]:
            answer = cnt
            break

        for df, dx, dy in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nf = cf + df
            nx = cx + dx
            ny = cy + dy
            if nf < 0 or nx < 0 or ny < 0 or nf >= L or nx >= R or ny >= C: continue
            if visited[nf][nx][ny]: continue
            if board[nf][nx][ny] == '#': continue
            visited[nf][nx][ny] = True
            q.append((nf, nx, ny, cnt + 1))
    if answer == 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(answer) +" minute(s).")
