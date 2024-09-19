import sys

input = sys.stdin.readline


N, M = map(int, input().split(' '))

num_list = list(map(int, input().split(' ')))
sum_list = [0]*N
sum_list[0] = num_list[0]
for i in range(1, N):
    sum_list[i] = sum_list[i-1] + num_list[i]

for i in range(M):
    a, b = map(int, input().split(' '))
    if a < 2:
        print(sum_list[b-1])
    else:
        print(sum_list[b-1]-sum_list[a-2])