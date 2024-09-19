import sys
import math
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

K, N = map(int, input().split(' '))

length_list = deque()
length_sum = 0
max_length = 0

for i in range(K):
    length_list.append(int(input()))
    length_sum += length_list[-1]
    
max = length_sum//N
min = 1
middle = (min + max)//2

def sum(middle):
    total = 0
    for i in range(K):
        total += length_list[i]//middle
    return total

while True:
    if N <= sum(middle):
        if max==min:
            print(str(middle))
            break
        min = middle
        middle = (min+max)//2
        if max - min == 1:
            if N <= sum(max):
                print(str(max))
                break
            else:
                print(str(min))
                break
    elif N > sum(middle):
        max = middle
        middle = (min+max)//2
        if max - min == 1:
            if N <= sum(max):
                print(str(max))
                break
            else:
                print(str(min))
                break
