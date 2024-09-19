import sys
import queue

input = sys.stdin.readline

N = int(input())

queue = queue.Queue()

for i in range(1,N+1):
    queue.put(i)

for i in range(N-1):
    queue.get()
    queue.put(queue.get())

print(queue.get())

# deque를 사용한 코드가 10배 정도 빠르다

# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# card = deque()

# for i in range(1, n+1):
#     card.append(i)
    
# while len(card) > 1:
#     card.popleft()
#     card.append(card.popleft())

# print(card[0])
# profile
# Hoojeong
