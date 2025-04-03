import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
board = [[char for char in input().strip()] for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if board[i][j] == '-':
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    curX, curY = queue.popleft()
                    for dx, dy in [(0, 1), (0, -1)]:
                        nx = curX + dx
                        ny = curY + dy
                        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                        if visited[nx][ny]: continue
                        if board[nx][ny] != board[i][j]: continue
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            else:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    curX, curY = queue.popleft()
                    for dx, dy in [(1, 0), (-1, 0)]:
                        nx = curX + dx
                        ny = curY + dy
                        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                        if visited[nx][ny]: continue
                        if board[nx][ny] != board[i][j]: continue
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            cnt += 1
print(cnt)