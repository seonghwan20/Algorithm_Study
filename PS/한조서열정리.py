# 그리디 알고리즘

import sys

input = sys.stdin.readline

N = int(input())

height_list = list(map(int, input().split(' ')))

max = 0
score = 0
H = height_list[0]

for i in range(N-1):
    if H > height_list[i+1]:
       score += 1
       if i+1 == N-1:
           if score > max:
               max = score
    else:
        if score > max:
            max = score
        H = height_list[i+1]
        score = 0
        
print(max)