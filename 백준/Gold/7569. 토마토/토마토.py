import sys
from collections import deque

input = sys.stdin.readline

# 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
# 익은 토마토 = 1, 안 익은 토마토 0, 빈칸 -1
M, N, H = map(int, input().split())

# x, y, z =
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
queue = deque()
already = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((h, n, m, 0))
                visited[h][n][m] = True
            if box[h][n][m] == 0:   #already가 False로 바뀌지 않는다면 0이 없다는 의미 => 이미 다 익은 상태
                already = False
ans = 0
def bfs():
    global ans
    while queue:
        h, x, y, time = queue.popleft()
        ans = time
        for dh, dx, dy in [(1, 0, 0), (-1,0,0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nh = h + dh
            nx = x + dx
            ny = y + dy
            if nh < 0 or nx < 0 or ny < 0 or nh >= H or nx >= N or ny >= M: continue
            if visited[nh][nx][ny]: continue
            if box[nh][nx][ny] == -1: continue
            queue.append((nh, nx, ny, time + 1))
            visited[nh][nx][ny] = True

bfs()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0 and not visited[h][n][m]: # 안익은게 남은 상태
                ans = -1
                
if already: #이미 다 익은 상태
    ans = 0

print(ans)