import heapq
import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(1, V + 1)}
dist = [10**9] * (V + 1)
for i in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

def dijkstra(node):
    pq = []
    dist[node] = 0
    heapq.heappush(pq, (0, node))
    while pq:
        cur_weight, current = heapq.heappop(pq)
        if dist[current] != cur_weight: continue
        for neighbor_weight, neighbor in graph[current]:
            if dist[neighbor] > dist[current] + neighbor_weight:
                dist[neighbor] = dist[current] + neighbor_weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
dijkstra(K)
ans = [str(d) if d != 10**9 else "INF" for d in dist[1:]]
print("\n".join(map(str,ans)))