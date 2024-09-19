import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for i in range(T):
    N, M = map(int, input().split(' '))
    priority = deque(list(map(int, input().split(' '))))
    document = deque([N for N in range(1,N+1)])
    
    doc = document[M]
    order = 1
    
    while True:
        if priority[0] == max(priority):
            if document[0] == doc:
                print(str(order) + '\n')
                break
            else:
                priority.popleft()
                document.popleft()
                order += 1
        else:
            priority.rotate(-1)
            document.rotate(-1)
            