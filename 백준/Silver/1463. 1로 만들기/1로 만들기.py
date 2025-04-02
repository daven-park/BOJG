import sys
from collections import deque

input = sys.stdin.readline

def bfs(n):
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(n)

    while queue:
        current = queue.popleft()

        if current == 1:
            return visited[1]

        for neighbor in [current - 1, current // 2 if current % 2 == 0 else 0, current // 3 if current % 3 == 0 else 0]:
            if neighbor > 0 and visited[neighbor] == 0:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)

N = int(input())
print(bfs(N))