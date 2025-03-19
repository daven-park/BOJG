import sys
from collections import deque

N, M = map(int, input().split())

maps = [[char for char in input()] for _ in range(N)]

ans = 0

def validate(nx, ny, visited):
    if nx < 0 or ny < 0 or nx >= N or ny >= M: return False
    if visited[nx][ny]: return False
    if maps[nx][ny] == 'W': return False
    return True

def bfs(x, y):
    global ans

    dir = [(1,0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    max_distance = 0
    while queue:
        curX, curY, weight = queue.popleft()
        for dx, dy in dir:
            nx, ny = curX + dx, curY + dy

            if validate(nx, ny, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, weight + 1))
                max_distance = max(max_distance, weight + 1)

    ans = max(ans, max_distance)

# 육지를 모두 체크하고 현재 시작 위치에서 가장먼 곳의 경로가 답으로 체크.

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            bfs(i, j)


print(ans)