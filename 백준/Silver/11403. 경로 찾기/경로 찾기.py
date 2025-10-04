import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dist = [[0] * N for _ in range(N)]

adj = [list(map(int, input().split())) for _ in range(N)]

def bfs(node, adj):
    visited = [False] * N
    q = deque()
    q.append(node)
    while q:
        current_node = q.popleft()
        for neighbor, conn in enumerate(adj[current_node]):
            if conn and not visited[neighbor]:
                visited[neighbor] = True
                dist[node][neighbor] = 1
                q.append(neighbor)


for i in range(N):
    bfs(i, adj)

for row in dist: print(*row)