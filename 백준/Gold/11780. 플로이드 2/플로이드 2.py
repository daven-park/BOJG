import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

dist = [[float("inf")] * (N + 1) for _ in range(N + 1)]
path = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0

for i in range(M):
    u, v, w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)
    path[u][v] = v #도착지가 지나친 경로니까

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]
# n개의 줄을 출력해야 한다. i번째 줄에 출력하는  j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다.
# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

#그 다음에는 n×n개의 줄을 출력해야 한다
def get_path(start, end):
    if path[start][end] == 0:
        return []
    result = [start]
    while start != end:
        start = path[start][end]
        result.append(start)
    return result

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == float("inf") or i == j:
            print(0)
        else:
            temp = get_path(i, j)
            print(len(temp), *temp)