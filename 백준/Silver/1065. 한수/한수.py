import sys

N = int(input())

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 1,000보다 작거나 같은 자연수 N
def hansu(num):
    if num < 100:
        return True

    num_list = [int(char) for char in str(num)]
    for idx in range(1, len(num_list) - 1):
        # 2b = a + c
        if 2 * num_list[idx] != num_list[idx - 1] + num_list[idx + 1]:
            return False
        
    return True

ans = 0
for i in range(1, N + 1):
    if hansu(i):
        ans += 1

print(ans)