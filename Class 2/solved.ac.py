import sys
import math
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = float(input())

def round(num):
    if (num - math.floor(num)) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)
        
if N == 0:
    print('0')
else:
    level_score_list = deque()
    temp = []
    level_score = 0

    for i in range(int(N)):
        temp.append(int(input()))

    temp.sort()

    level_score_list = deque(temp)

    cut_line = round((N/100)*15)

    for i in range(cut_line):
        level_score_list.pop()
        level_score_list.popleft()

    for i in range(len(level_score_list)):
        level_score += level_score_list.pop()
        
    print(str(round(level_score/(int(N)-(cut_line*2)))))