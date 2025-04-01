import sys

input = sys.stdin.readline

# 연산자 별로 방문체크를 통해 사용했는지 판단
# 백트래킹으로 다음 것도 들어가기
N = int(input())
numbers = [int(num) for num in input().split()]
opers = [int(num) for num in input().split()]   # + - * /
max_result = -int(1e9)
min_result = int(1e9)

def dfs(total, k):
    global max_result, min_result
    if k == N:
        if max_result < total: max_result = total
        if min_result > total: min_result = total
        return

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            if i == 0:
                dfs(total + numbers[k], k + 1)
            elif i == 1:
                dfs(total - numbers[k], k + 1)
            elif i == 2:
                dfs(total * numbers[k], k + 1)
            else:
                if total < 0:
                    dfs(-(-total // numbers[k]), k + 1)
                else:
                    dfs(total // numbers[k], k + 1)
            opers[i] += 1
    return

dfs(numbers[0], 1)
print(max_result)
print(min_result)