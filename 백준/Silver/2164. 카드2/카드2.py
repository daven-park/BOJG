import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cards = deque([num for num in range(1, N + 1)])

while len(cards) > 1:
    # 제일 위카드 바닥에 버리기
    cards.popleft()
    # 제일 위카드 제일 아래롤 옮김
    cards.append(cards.popleft())

result = [cards[0]]
sys.stdout.write(str(*result))
sys.stdout.close()
