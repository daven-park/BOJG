import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph_heavy = {i:[] for i in range(N + 1)}
graph_light = {i:[] for i in range(N + 1)}
for i in range(M):
    s, e = map(int,input().split())
    graph_heavy[s].append(e)
    graph_light[e].append(s)

def dfs(graph, visited, node):
    cnt = 0
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            cnt += 1 + dfs(graph, visited, neighbor)
    return cnt

mid = (N + 1) // 2

result = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)

    heavy = dfs(graph_heavy, visited, i)
    if heavy >= mid:
        result += 1
        continue

    visited = [False] * (N + 1)
    light = dfs(graph_light, visited, i)
    if light >= mid:
        result += 1

print(result)