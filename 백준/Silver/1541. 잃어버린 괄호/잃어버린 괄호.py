import sys
import re

input = sys.stdin.readline

# 마이너스 가 붙은 값을 최대로 만들기

# 마이너스 뒤의 값들이 +이면 전부 먼저 처리하기

string = input()

tokens = re.findall(r'\d+|[+\-]', string)

total = 0
i = 0
while i < len(tokens):
    if tokens[i] == '-':    # 다음 숫자부터 +만나기 전 숫자까지 모두 더하고 -붙여서 total
        i += 1
        temp = 0
        while  i < len(tokens) and tokens[i] != "-" :
            if tokens[i] != "+":    # 숫자이면
                temp += int(tokens[i])
            i += 1
        total -= temp
    elif tokens[i] == '+':  #
        i += 1
    else:
        total += int(tokens[i])
        i += 1
print(total)