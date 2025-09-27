import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    M, N = map(int, input().split())
    answer = -1
    board = [list(map(str, input().strip())) for _ in range(N)]
    INF = int(1e9)
    fire_times = [[INF] * M for _ in range(N)]

    start = None
    fire_start = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == '@':
                start = (i, j)
            if board[i][j] == '*':
                fire_start.append((i, j))
                fire_times[i][j] = 1
            if board[i][j] == '#':
                fire_times[i][j] = -1

    # 불 지피기
    visited = [[False] * M for _ in range(N)]
    q = deque([])
    for x, y in fire_start:
        q.append((x, y, 1))
        visited[x][y] = True

    while q:
        curX, curY, time = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if fire_times[nx][ny] == -1: continue
            fire_times[nx][ny] = time + 1
            q.append((nx, ny, time + 1))
            visited[nx][ny] = True

    # 사람 움직이기
    visited = [[False] * M for _ in range(N)]
    q = deque([(start[0], start[1], 1)])
    visited[start[0]][start[1]] = True
    while q:
        curX, curY, time = q.popleft()
        if curX == 0 or curY == 0 or curX == N - 1 or curY == M - 1:
            answer = time
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if fire_times[nx][ny] == -1: continue
            if fire_times[nx][ny] <= time + 1:
                continue
            q.append((nx, ny, time + 1))
            visited[nx][ny] = True

    if answer == -1:
        print("IMPOSSIBLE")
    else:
        print(answer)
