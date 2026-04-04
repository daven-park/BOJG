import sys
from collections import deque

input = sys.stdin.readline


# 1 <= N, M  <= 100
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
ex_air = [[False] * M for _ in range(N)]
time = 0
answer = 0

def can_melt():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1: return True
    return False

def air_check():
    q = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:
        curX, curY = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = curX + dx
            ny = curY + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            q.append((nx, ny))
            ex_air[nx][ny] = True

def melt():
    global board
    remove_cheese = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            is_melt = False
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = i + dx
                ny = j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                if board[nx][ny] == 1: continue
                if not ex_air[nx][ny]: continue
                is_melt = True

            if is_melt:
                remove_cheese.append((i, j))
    cnt = len(remove_cheese)
    for x, y in remove_cheese:
        board[x][y] = 0

    return cnt

while True:
    if not can_melt():
        break
    air_check()
    answer = melt()
    time += 1

print(time)
print(answer)