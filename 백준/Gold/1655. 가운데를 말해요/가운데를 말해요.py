import heapq
import sys

input = sys.stdin.readline

N = int(input())

minh = []
maxh = []
for i in range(N):
    num = int(input())
    if len(minh) == len(maxh):
        heapq.heappush(maxh, -num)
    else:
        heapq.heappush(minh, num)
    # 최대힙 루트가 최소힙모다 크다면 중앙값 유지를 위해 값 변경
    if minh and -maxh[0] > minh[0]:
        maxNum = -heapq.heappop(maxh)
        minNum = heapq.heappop(minh)
        heapq.heappush(maxh, -minNum)
        heapq.heappush(minh, maxNum)

    print(-maxh[0])