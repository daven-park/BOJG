import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

# 무방향 비순환 그래프
graph = defaultdict(list)
answer = 0
for i in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False] * (N + 1)
def dfs(current):
    global answer
    first = 0
    second = 0
    for neighbor, weight in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            child = dfs(neighbor) + weight
            if child > first:
                second = first
                first = child
            elif child > second:
                second = child

    answer = max(answer, first + second)
    return first

visited[1] = True
dfs(1)
print(answer)