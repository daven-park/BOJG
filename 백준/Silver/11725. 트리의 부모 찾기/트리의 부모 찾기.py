import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for i in range(N - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

parent = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(current, node):
    parent[current] = node
    visited[current] = True

    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, current)

def bfs(node):
    queue = deque([node])
    visited = [False] * (N + 1)
    visited[node] = True
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parent[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)

dfs(1, 1)
#bfs(1)
print("\n".join(map(str,parent[2:])))