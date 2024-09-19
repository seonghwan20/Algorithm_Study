import sys

input = sys.stdin.readline

N = int(input())

i=0

n=N

m = []

while n-3>0:
    if n%5 == 0:
        m.append(i+int(n/5))
        break
    n -= 3 
    i += 1

if N%3 == 0:
    m.append(int(N//3))
    
if len(m)<1:
    print(-1)
else:
    print(min(m))