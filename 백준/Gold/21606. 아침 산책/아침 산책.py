import sys
from collections import defaultdict

input = sys.stdin.readline

# 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다. => 무방향 그래프
# N개의 장소를(정점 N), N - 1개의 길(간선 N - 1)이 있는
# 시작점과 도착점을 정하고(start, end)
# 트리 위의 단순 경로(같은점을 여러번 지나지 않음) 방문체크 visited
# N개 장소중 일부는 실내, 나머지는 실외 place = 1 -> inside, 0 -> outside
# start, end 모두 place[0]
# 서로 다른 산책경로 찾기

N = int(input())

graph = defaultdict(list)
place = [int(char) for char in "0" + input().strip()]
for i in range(N - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
count = 0
visited = [0] * (N + 1)

def dfs_outside(node): # 사이에 실외가 있는 구간 카운트
    visited[node] = True
    inside_count = 0

    for neighbor in graph[node]:
        if place[neighbor] == 1:
            inside_count += 1
        elif not visited[neighbor]:
            inside_count += dfs_outside(neighbor)

    return inside_count


for i in range(1, N + 1):
    if place[i] == 0 and not visited[i]:
        k = dfs_outside(i)
        count += k * (k - 1)

for i in range(1, N + 1):
    if place[i] == 1:
        for neighbor in graph[i]:
            if place[neighbor] == 1:
                count += 1
print(count)