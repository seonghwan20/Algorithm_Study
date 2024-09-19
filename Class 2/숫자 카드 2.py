import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

num_list1 = list(map(int, input().split(' ')))

M = int(input())

num_list2 = list(map(int, input().split(' ')))

num = [0]*20000001

for i in range(N):
    num[num_list1[i]+10000000] += 1

for i in range(M):
    print(str(num[num_list2[i]+10000000]) + ' ')