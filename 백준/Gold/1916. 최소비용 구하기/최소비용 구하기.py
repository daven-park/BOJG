import heapq
import sys

input = sys.stdin.readline

# 한 도시 출발 다른도시 도착 => 방향그래프
# 0 <= 버스비용 <= 100000
# 최소비용 출력 : 다익스트라
# 만약 최소비용이 음수 : 플로이드와샬

N = int(input())    # 정점
M = int(input())    # 간선

graph = {i : [] for i in range(1, N + 1)}
dist = [10**9] * (N + 1)
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

start, end = map(int, input().split())  # 출발 도착 정답

def dijkstra(node):
    pq = []
    dist[node] = 0
    heapq.heappush(pq, (0, node))

    while pq:
        cur_weight, cur_node = heapq.heappop(pq)
        if dist[cur_node] != cur_weight: continue
        for next_weight, next_node in graph[cur_node]:
            new_weight = dist[cur_node] + next_weight
            if dist[next_node] > new_weight:
                dist[next_node] = new_weight
                heapq.heappush(pq, (new_weight, next_node))


dijkstra(start)
print(dist[end])