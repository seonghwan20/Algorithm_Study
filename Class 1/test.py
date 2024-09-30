import sys

input = sys.stdin.readline

T = int(input())

mnt_list = list(map(int, input().split(' ')))

max = 0
cnt = 0
idx = 0
i = 1
while(idx+i < T):
    if mnt_list[idx] > mnt_list[idx+i]:
        cnt += 1
        i += 1
    else:
        if cnt > max :
            max = cnt
        cnt = 0
        idx = idx + i
        i = 1

print(max)