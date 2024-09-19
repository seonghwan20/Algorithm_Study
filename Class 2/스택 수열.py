import sys

input = sys.stdin.readline

n = int(input())

input_list = []
num_list = [ n for n in range(1,n+1)]
stack = [0]
answer = []
temp = True

for i in range(n):
    input_list.append(int(input()))
    
for i in range(n):
    num = input_list.pop(0)
    while num > stack[-1]:
        stack.append(num_list.pop(0))
        answer.append('+')
    if num == stack[-1]:
        stack.pop(-1)
        answer.append('-')
    if num < stack[-1]:
        print('NO')
        temp = False
        break
    
if temp:
    print(*answer, sep = '\n')