import collections
import sys
from collections import deque

input = sys.stdin.readline

# 단방향 도로 => 방향 그래프
# N 정점, M 간선, 가중치 1
# 최단거리 k인 모든 도시 번호 출력 => 정점별 최단거리 저장 리스트 사용
N, M, K, X = map(int, input().split())
shortpath = [-1] * (N + 1)
shortpath[X] = 0
graph = collections.defaultdict(list)
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

def bfs(node):
    queue = deque()
    queue.append((node, 0))
    while queue:
        current, dist = queue.popleft()
        for neighbor in graph[current]:
            if shortpath[neighbor] != -1: continue
            shortpath[neighbor] = dist + 1
            queue.append((neighbor, dist + 1))

bfs(X)
ans = [num for num in range(1, N + 1) if shortpath[num] == K]
print(-1 if len(ans) == 0 else "\n".join(map(str, ans)))
