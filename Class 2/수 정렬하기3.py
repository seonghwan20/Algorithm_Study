# import sys

# N = int(sys.stdin.readline().rstrip())

# count = [0 for i in range(10001)]

# for i in range(N):
#     num = int(sys.stdin.readline().rstrip())
#     count[num] += 1
    
# for i in range(1, 10001):
#     if count[i] > 0:
#         sys.stdout.write(f"{i}\n" * count[i])

import sys

N = int(sys.stdin.readline().rstrip())
count = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    count[number] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(f'{i}\n')

# 출력할 때는 곱해서 출력하면 메모리를 많이 잡아먹는다. 되도록이면 반복문으로 출력.