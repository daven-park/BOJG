import sys

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
selected = []
isUsed = [False] * 10
def func(k : int):
    if k == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(0, N):
        if not isUsed[i]:
            isUsed[i] = True
            selected.append(arr[i])
            func(k + 1)
            isUsed[i] = False
            selected.pop()

func(0)