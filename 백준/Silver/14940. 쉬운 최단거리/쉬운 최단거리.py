import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = [[int(char) for char in input().split()] for _ in range(N)]

start = None
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            start = (i, j)
            
ans = [[-1] * M for _ in range(N)]
def bfs():
    queue = deque([(start[0], start[1], 0)])
    ans[start[0]][start[1]] = 0
    while queue:
        curX, curY, dist = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if ans[nx][ny] != -1: continue
            if maps[nx][ny] != 1: continue
            queue.append((nx, ny, dist + 1))
            ans[nx][ny] = dist + 1

bfs()

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            print(0, end =' ')
        else:
            print(ans[i][j], end = ' ')
    print()