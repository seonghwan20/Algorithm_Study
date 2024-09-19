import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split(' '))

coin_list = deque()

for i in range(N):
    coin_list.append(int(input()))
    
coin_min = 0

while len(coin_list) > 0:
    coin = coin_list.pop()
    coin_min += K//coin
    K %= coin

print(coin_min)