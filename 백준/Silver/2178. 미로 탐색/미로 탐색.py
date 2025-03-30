import collections
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maps = [[int(char) for char in "".join(input().strip())] for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = 0
def bfs (x, y):
    global ans
    queue = collections.deque()
    queue.append((x, y, 1))
    visited[x][y] = True
    while queue:
        curX, curY, count = queue.popleft()
        if curX == N - 1 and curY == M - 1:
            ans = count
            break
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if maps[nx][ny] == 0: continue
            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True
bfs(0, 0)
print(ans)