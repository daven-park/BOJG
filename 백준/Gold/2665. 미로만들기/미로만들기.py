import heapq
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [[int(char) for char in input().strip()] for _ in range(N)]
dist = [[10**9] * N for _ in range(N)]

def bfs(x, y):
    pq = []
    heapq.heappush(pq, (0, x, y))
    dist[x][y] = 0
    while pq:
        curdist, curx, cury = heapq.heappop(pq)
        if curdist > dist[curx][cury]: continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + curx
            ny = dy + cury
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            new_dist = curdist + (1 if board[nx][ny] == 0 else 0)
            if new_dist < dist[nx][ny]:
                dist[nx][ny] = new_dist
                heapq.heappush(pq, (new_dist, nx, ny))

bfs(0, 0)
print(dist[N - 1][N - 1])