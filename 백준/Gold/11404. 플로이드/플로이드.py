import heapq
import sys

input = sys.stdin.readline

# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
# 모든 도시 쌍 => 다익스트라 x　플로이드 와샬 의심
# 비용은 100,000보다 작거나 같은 자연수이다. 양수(음수와 사이클이 존재하는것이 아니기 때문에 벨만포드 x)
# 2 <= N <= 100 도시 -> 정점
# 1 <= M <= 100000 버스 -> 간선
# 버스는 사용할때 필요 비용이 있다 -> 가중치

N = int(input())
M = int(input())
dist = [[10**9] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    s, e, w = map(int, input().split())
    dist[s][e] = min(dist[s][e], w)

for i in range(1, N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == 10**9:
            print(0, end = ' ')
        else :
            print(dist[i][j], end =' ')
    print()