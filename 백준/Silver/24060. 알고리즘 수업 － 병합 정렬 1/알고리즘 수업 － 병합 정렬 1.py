import sys
from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0        # 저장 횟수
result = -1      # K번째 저장값

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    global count, result
    i, j = p, q + 1
    temp = []

    while i <= q and j <= r:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= q:
        temp.append(a[i])
        i += 1

    while j <= r:
        temp.append(a[j])
        j += 1

    t = 0
    for idx in range(p, r + 1):
        count += 1
        if count == K:
            result = temp[t]
        a[idx] = temp[t]
        t += 1

merge_sort(A, 0, N - 1)
print(result)