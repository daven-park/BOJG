import sys
import random

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
N = int(input())

input = sys.stdin.readline
numbers = [int(input()) for i in range(N)]
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

def random_partition(arr, low, high):
    random_pivot = random.randrange(low, high)
    arr[low], arr[random_pivot] = arr[random_pivot], arr[low]
    return arr[low]

def quick_sort(a, left, right) :
    if left >= right: return
    pl = left
    pr = right
    pivot = random_partition(a, left, right)

    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    quick_sort(a, left, pr)
    quick_sort(a, pl, right)

quick_sort(numbers, 0, len(numbers) - 1)

sys.stdout.write("\n".join(map(str, numbers)))
