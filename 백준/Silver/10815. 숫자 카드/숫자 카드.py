import sys

input = sys.stdin.readline

# N(1 ≤ N ≤ 500,000)
# M(1 ≤ M ≤ 500,000)
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
targets = list(map(int, input().split()))
answer = [0] * M

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for i in range(M):
    target = targets[i]
    answer[i] = 1 if binary_search(cards, target) != -1 else 0

print(*answer)