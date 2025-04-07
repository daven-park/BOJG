import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    rank = []
    for i in range(N):
        s, e = map(int, input().split())
        rank.append((s, e))
    rank.sort()
    stack = []
    minV = N + 1
    for current in rank:
        first, second = current
        if len(stack) == 0: # 비어있으면 바로 넣기
            stack.append((first, second))
            minV = second
        else:
            if second < minV:
                stack.append((first, second))
                minV = second

    print(len(stack))