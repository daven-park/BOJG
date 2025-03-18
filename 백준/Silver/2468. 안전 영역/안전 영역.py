import sys
from collections import deque

N = int(input())

input = sys.stdin.readline

maps = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

def bfs(x, y, curheight, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        current = queue.popleft()
        for d in range(4):
            nx = current[0] + dx[d]
            ny = current[1] + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if visited[nx][ny] or maps[nx][ny] <= curheight: continue
            visited[nx][ny] = True
            queue.append((nx, ny))

maxHeight = max(map(max, maps))

for curHeight in range(maxHeight):
    safeArea = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and maps[i][j] > curHeight:
                bfs(i, j, curHeight, visited)
                safeArea += 1
    ans = max(safeArea, ans)

print(ans)