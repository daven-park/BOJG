import sys
import bisect

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


ans = []
for num in arr:
    pos = bisect.bisect_left(ans, num)
    if pos == len(ans): # 이분탐색으로 가장 끝이라면 가장 크므로 길이를 늘려야함
        ans.append(num)
    else:               # 가장 끝이 아니라면 해당하는 위치에 값을 치환한다.
        ans[pos] = num

print(len(ans))