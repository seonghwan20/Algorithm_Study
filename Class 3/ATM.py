import sys

input = sys.stdin.readline

N = int(input())

time_list = list(map(int, input().split(' ')))

new_time_list = sorted(time_list)

num = N

total = 0

for i in range(N):
    total += new_time_list[i]*num
    num -= 1
    
print(total)