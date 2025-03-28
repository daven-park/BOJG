import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

adjlist = defaultdict(list)
for i  in range(0, M):
    start, end = map(int, input().split())
    adjlist[start].append(end)
    adjlist[end].append(start)

for node in adjlist:
    adjlist[node].sort()

visited = [False] * (N + 1)
def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for neighbor in adjlist[node]:
        if not visited[neighbor]:
            dfs(neighbor)

def bfs(node):
    queue = deque([node])
    visited_bfs = {node}

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in adjlist.get(current, []):
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

dfs(V)
print()
bfs(V)