import sys
from collections import deque

input = sys.stdin.readline

# N <= 1000 M <= 1000
N, M = map(int, input().split())
# (1,1) = 0 , (N, M) = 0

board = [[int(num) for num in input().strip()] for _ in range(N)]

answer = -1
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
def bfs(x, y):
    global answer
    queue = deque()
    visited[x][y][0] = True
    queue.append((x, y, 1, False))
    while queue:
        curX, curY, cnt, flag = queue.popleft()
        if curX == N - 1 and curY == M - 1:
            answer = cnt
            return
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if board[nx][ny] == 1 and not flag and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, cnt + 1, True))
                continue
            if board[nx][ny] == 0 and not visited[nx][ny][flag]:
                visited[nx][ny][flag] = True
                queue.append((nx, ny, cnt + 1, flag))

bfs(0, 0)

print(answer)