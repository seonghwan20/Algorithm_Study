import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

money_list = deque()

for i in range(K):
    money = int(input())
    if money == 0:
        money_list.pop()
    else:
        money_list.append(money)
        
print(sum(money_list))