import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
isUsed = [False] * 10
output = []

def func(start, selected):
    if len(selected) == M:
        print(*selected)
        return

    for i in range(start, N):
            func(i, selected + [arr[i]])

func(0, [])