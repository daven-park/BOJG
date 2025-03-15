import sys

N = int(input())

counter = [False] * 10001

# 소수 구하기
for i in range(2, int(10001 ** 0.5) + 1):
    if not counter[i]:
        for j in range(i * i, 10001, i):
            counter[j] = True

prime_list = [i for i, prime in enumerate(counter) if not prime]

# 투포인터
def find_prime_twopointer(target, prime_list):
    ans = []
    left = 0
    right = len(prime_list) - 1
    while left <= right:
        total = prime_list[left] + prime_list[right]
        if total == target:
            ans.append((prime_list[left], prime_list[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return ans

for t in range(N):
    target = int(input())
    answer = find_prime_twopointer(target, prime_list).pop()
    print(answer[0], answer[1])
    
sys.stdout.close()
