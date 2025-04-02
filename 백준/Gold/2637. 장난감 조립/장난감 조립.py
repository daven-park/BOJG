import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {i : [] for i in range(N + 1)}

in_degree = [0] * (N + 1)
parts = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    s, e, w = map(int, input().split())
    graph[e].append((s, w))
    in_degree[s] += 1

queue = deque()
for i in range(1, N):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    for neighbor, weight in graph[current]:
        if not any(parts[current]):
            parts[neighbor][current] += weight
        else:
            for i in range(1, N + 1):
                parts[neighbor][i] += parts[current][i] * weight
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

for i in range(1, N):
    if parts[N][i] > 0:
        print(i, parts[N][i])
