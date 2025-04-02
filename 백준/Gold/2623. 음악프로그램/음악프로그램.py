import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}

in_degree = [0] * (N + 1)

for i in range(M):
    orders = list(map(int, input().split()))
    for j in range(1, orders[0]):
        graph[orders[j]].append(orders[j + 1])
        in_degree[orders[j + 1]] += 1
_list = [idx for idx in range(1, N + 1) if in_degree[idx] == 0]
queue = deque(_list)
result = []
while queue:
    current = queue.popleft()
    result.append(current)
    for neighbor in graph[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)