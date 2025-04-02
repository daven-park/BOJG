import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

# 빙산의 높이는 해당 칸의 동서남북 네방향으로 붙어있는 0의 개수만큼 줄어든다
# 0 보다는 줄지 않는다
#  빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)

# 다 녹을때까지 두덩어리 이상 안되면 0 출력

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

time = 0

def dfs(x, y, visited):
    visited[x][y] = True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = dx + x
        ny = dy + y
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if visited[nx][ny]: continue
        if maps[nx][ny] == 0:continue
        dfs(nx, ny, visited)

def bfs(x, y, visited, melting):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        curX, curY = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if maps[nx][ny] == 0:
                melting[curX][curY] += 1
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True

def 빙산분리체크(): # dfs로 연결되었는지 찾기 연결 요소의 개수
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0 and not visited[i][j]:
                dfs(i, j, visited)
                cnt += 1
    return cnt

def 빙산녹이기():
    melting = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0 and not visited[i][j]:
                bfs(i, j, visited, melting)

    for i in range(N):
        for j in range(M):
            if melting[i][j] != 0:
                maps[i][j] = max(maps[i][j] - melting[i][j], 0)
    return

while True:
    cnt = 빙산분리체크()
    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        print(time)
        break
    빙산녹이기()
    time += 1