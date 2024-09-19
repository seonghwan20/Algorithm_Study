import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

scores = deque()

for i in range(N):
    scores.append(int(input()))
    
stairs = deque([0, 0, 0] for i in range(N)) # 01 10 11 의 경우의 수


if N > 3:
    stairs[0][0] = 0
    stairs[0][1] = scores[0]

    stairs[1][0] = stairs[0][0] + scores[1]
    stairs[1][1] = stairs[0][1]
    stairs[1][2] = stairs[0][1] + scores[1]

    for i in range(2, N-2):    
        stairs[i][0] = stairs[i-1][1] + scores[i]
        stairs[i][1] = max(stairs[i-1][0], stairs[i-1][2])
        stairs[i][2] = stairs[i-1][0] + scores[i]
        
    stairs[N-2][0] = stairs[N-3][1] + scores[N-2]
    stairs[N-2][1] = max(stairs[N-3][0], stairs[N-3][2])

    print(max(stairs[N-2]) + scores[N-1])
elif N == 3:
    print(sum(scores) - min(scores))
else:
    print(sum(scores))
        

