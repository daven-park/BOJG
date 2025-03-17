import sys
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

N = int(input())
numbers = list(map(int, input().split()))

ans = 0

visited = [False] * N

def getSum(selected : list):
    return sum(abs(selected[i] - selected[i + 1]) for i in range(len(selected) - 1))

def recursive(selected):
    global ans
    if len(selected) == N:
        ans = max(ans, getSum(selected))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected.append(numbers[i])
            recursive(selected)
            selected.pop()
            visited[i] = False

recursive([])
print(ans)