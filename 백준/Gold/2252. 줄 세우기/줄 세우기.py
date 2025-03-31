import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i : [] for i in range(1, N + 1)}

in_degree = [0] * (N + 1)

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    in_degree[e] += 1

result = []
def bfs(node):
    queue = deque([idx for idx, num in enumerate(in_degree[1:], start=1) if num == 0])
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

bfs(1)
print(*result)
