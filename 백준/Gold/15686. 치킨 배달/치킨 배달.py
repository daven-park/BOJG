import sys
from collections import defaultdict, deque
from itertools import combinations
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []

def get_distance(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i, j))
        if board[i][j] == 1:
            houses.append((i, j))

answer = float('inf')

for comb in combinations(range(len(chickens)), M):
    total = 0
    for x, y in houses:
        min_dist = float('inf')
        for j in comb:
            curX, curY = chickens[j]
            dist = get_distance(x, curX, y, curY)
            if  min_dist > dist:
                min_dist = dist
        total += min_dist
        # 가지치기(정답보다 크면 갱신 x
        if total >= answer:
            break
    if total < answer:
        answer = total

print(answer)