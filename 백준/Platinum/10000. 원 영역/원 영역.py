import sys

input = sys.stdin.readline

N = int(input())

stack = []
circles = []
area = 1


# x좌표 기준 원의 시작/끝 이벤트 생성
def create_circle_orders(circles):
    orders = []
    for idx, circle in enumerate(circles):
        x, r = circle
        orders.append(['(', x - r, 0])
        orders.append([')', x + r, 0])
    orders.sort(key=lambda x: (x[1], -ord(x[0])))   # 정렬하여 좌표가 왼쪽부터, 원이 큰 순서대로 정렬
    return orders

for _ in range(N):
    x, r = map(int, input().split())
    circles.append([x, r])

orders = create_circle_orders(circles)


for i in range(N * 2):
    bracket, pos, status = orders[i]
    if len(stack) == 0:
        stack.append(orders[i])
        continue

    if bracket == ')':
        if stack[-1][2] == 0 :
            area += 1
        elif stack[-1][2] == 1:
            area += 2
        stack.pop()
        if i != N * 2 - 1:
            if orders[i + 1][1] != pos:
                stack[-1][2] = 0
    else:
        if stack[-1][1] == pos:
            stack[-1][2] = 1
            stack.append(orders[i])
        else:
            stack.append(orders[i])


result = [str(area)]
sys.stdout.write(" ".join(result))
sys.stdout.close()
