import sys

input = sys.stdin.readline

N = int(input())

lis = []

for i in range(N):
    lis.append(list(map(int, input().split(' '))))
    

    
lis.sort(key = lambda x:( x[1], x[0] ))

for i in range(N):
    print(str(lis[i][0]) + ' ' + str(lis[i][1]))