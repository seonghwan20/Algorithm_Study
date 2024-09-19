import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

queue = deque()

N = int(input())

for i in range(N):
    inst = list(map(str, input().rstrip().split(' ')))
    if inst[0] == 'push':
        queue.append(inst[1])
    elif inst[0] == 'pop':
        if len(queue) == 0:
            print('-1' + '\n')
        else:
            print(str(queue.popleft()) + '\n')
    elif inst[0] == 'size':
        print(str(len(queue)) + '\n')
    elif inst[0] == 'empty':
        if len(queue) == 0:
            print('1' + '\n')
        else:
            print('0' + '\n')
    elif inst[0] == 'front':
        if len(queue) == 0:
            print('-1' + '\n')
        else:
            print(str(queue[0]) + '\n')
    elif inst[0] == 'back':
        if len(queue) == 0:
            print('-1' + '\n')
        else:
            print(str(queue[-1]) + '\n')
