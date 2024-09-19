import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

D = set()
B = set()

i = 0

while i < M:
    D.add(input().rstrip())
    i += 1
    
i = 0

while i < N:
    B.add(input().rstrip())
    i += 1
    
C = D.intersection(B)

C = list(C)
C.sort()

print(len(C))
for i in C:
    print(i)