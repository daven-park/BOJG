N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

left = 0
right = houses[len(houses) - 1]

ans = 0

def checkIptime(dist, count) -> bool :
    start_idx = 0
    count -= 1
    for i in range(1, len(houses)):
        if houses[start_idx] + dist <= houses[i]:
            count -= 1
            start_idx = i
            if count == 0:
                return True
            
    return False

while left <= right:
    mid = (left + right) // 2
    if not checkIptime(mid, C):
        right = mid - 1
    elif checkIptime(mid, C):
        ans = max(mid, ans)
        left = mid + 1

print(ans)