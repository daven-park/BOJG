import sys

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
selected = []
visited = [False] * N

def permutation(count):
    if count == M:
        print(*selected)
        return
    prev = None
    for i in range(0, N):
        if not numbers[i] == prev:
            selected.append(numbers[i])
            permutation(count + 1)
            selected.pop()
            prev = numbers[i]
permutation(0)