import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

min_kevin = float('inf')
answer = -1
def bfs(node):
    q = deque([])
    visited = [False] * (N + 1)
    temp = 0
    visited[node] = True
    q.append((node, 0))
    while q:
        current, step = q.popleft()
        temp += step
        for neighbor in graph[current]:
            if visited[neighbor]: continue
            visited[neighbor] = True
            q.append((neighbor, step + 1))
    return temp

for start in range(1, N + 1):
    total = bfs(start)
    if total < min_kevin:
        min_kevin = total
        answer = start

print(answer)