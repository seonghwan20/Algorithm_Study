import sys
input = sys.stdin.readline
N, K = map(int, input().split(' '))

k = K

l = [i for i in range(1,N+1)]
answer =[]

while True:
    if not len(l):
        break
    if k > len(l) :
        k %= len(l)
    answer.append(l[k-1])
    del l[k-1]
    if k == len(l)+1 or k == 0:
        k = K
    else:
        k += K-1
        
print('<', end='')
for i in answer:
    if i == answer[-1]:
        print(i, end='')
        break
    print(i, end=', ')
print('>')