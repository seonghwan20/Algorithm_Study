# 비트마스킹

import sys

input = sys.stdin.readline

N = int(input())

answer = 0
src = bin(N)[2:]
for i in range(len(src)):
    answer += (3**i)*int(src[-i-1])
    
print(answer)