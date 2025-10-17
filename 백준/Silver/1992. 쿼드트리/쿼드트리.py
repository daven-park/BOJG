import sys

input = sys.stdin.readline

N = int(input())

board = [[ch for ch in input().strip()] for _ in range(N)]

def board_check(x, y, size):
    start = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != start:
                return -1
    return start

answer = ""
def dfs(x, y, size):
    global answer
    result = board_check(x, y, size)
    if result != -1:
        answer += result
    else:
        answer += "("
        dfs(x, y, size // 2)
        dfs(x, y + size // 2, size // 2)
        dfs(x + size // 2, y, size // 2)
        dfs(x + size // 2, y + size // 2, size // 2)
        answer += ")"

dfs(0, 0, N)
print(answer)