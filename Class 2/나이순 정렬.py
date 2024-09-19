import sys
input = sys.stdin.readline

N = int(input())

inf = []

for i in range(N):
    inf.append(list(map(str, input().split(' '))))
    
inf.sort(key = lambda x:int(x[0]))

for i in inf:
    print(i[0], end= ' ')
    print(i[1], end= '')