import sys

# 입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.
x, y = map(int, input().split())

T = int(input())

y_list = [0, y]
x_list = [0, x]

# 위치들을 리스트에 넣고 
for t in range(T):
    direction, val = map(int, input().split())
    # 0 = y,  1 = x
    if direction == 1:
        x_list.append(val)
    else:
        y_list.append(val)
        
# 정렬해서 
y_list.sort()
x_list.sort()

# 해당 값들의 차이를 구한다.
y_diff_list = [y_list[i] - y_list[i - 1] for i in range(1, len(y_list))]
x_diff_list = [x_list[i] - x_list[i - 1] for i in range(1, len(x_list))]

# 리스트중 가장 큰 값끼리의 곱이다
print(max(y_diff_list) * max(x_diff_list))