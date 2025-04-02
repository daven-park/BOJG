import copy
import heapq
import sys
from collections import deque

input = sys.stdin.readline

# 최소비용 구하기
#항상 시작점 도착점 경로 존재

# 도시(정점), 버스(간선)

N = int(input())
M = int(input())

graph = {i:[] for i in range(N + 1)}
dist = [10**9] * (N + 1)

for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())

pq = []
heapq.heappush(pq, (0, start))
dist[start] = 0
distance = [[] for _ in range(N+1)]
distance[start].append(start)
while pq:
    current_dist, current_node = heapq.heappop(pq)
    if dist[current_node] < current_dist: continue
    for next_dist, neighbor in graph[current_node]:
        new_dist = current_dist + next_dist
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))
            _list = copy.deepcopy(distance[current_node])
            _list.append(neighbor)
            distance[neighbor] = _list


print(dist[end])
print(len(distance[end]))
print(*distance[end])