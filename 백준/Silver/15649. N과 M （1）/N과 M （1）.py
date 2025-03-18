import sys

N, M = map(int, input().split())

arr = []
isUsed = [False] * 10

def func(k : int):
    if k == M:
        print(" ".join(map(str, arr[:M])))

    for i in range(1, N + 1):
        if not isUsed[i]:
            arr.append(i)
            isUsed[i] = True
            func(k + 1)
            isUsed[i] = False
            arr.pop()
func(0)