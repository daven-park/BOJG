import sys
from collections import deque

input = sys.stdin.readline

#  회의의 시작시간과 끝나는 시간이 같을 수도 있다
N = int(input()) # 회의의 수

# 시작하는 시간으로 정렬한 뒤 하나씩 완전탐색
intervals = []
for i in range(N):
    s, e = map(int, input().split())

    intervals.append((s, e))
intervals.sort(key= lambda x : (x[1], x[0]))
ans = 0
currentTime = 0
for start, end in intervals:
    if currentTime <= start:
        currentTime = end
        ans += 1
print(ans)
# 둘의 차가 짧은 것부터 정렬해버리기?