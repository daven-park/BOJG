N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
maxHeight = 0
while left <= right:
    mid = (left + right) // 2
    cutedTrees = sum(tree - mid for tree in trees if (tree - mid) > 0)
    if cutedTrees >= M:
        left = mid + 1
        maxHeight = max(maxHeight, mid)
    elif cutedTrees < M:
        right = mid - 1
print(maxHeight)