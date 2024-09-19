import sys

input = sys.stdin.readline

N = int(input())

network = [[] for i in range(N)]
virus_list = [0 for i in range(N)]
virus_list[0] = 1
M =int(input())

for i in range(M):
    networking = list(map(int, input().split(' ')))
    network[networking[0]-1].append(networking[1])
    network[networking[1]-1].append(networking[0])
    
for i in range(N):
    network[i] = list(set(network[i]))

def virus(cpu):    
    for i in range(len(network[cpu-1])):
        cpu_num = network[cpu-1][i]
        if virus_list[cpu_num-1] != 1:
            virus_list[cpu_num-1] = 1
            virus(cpu_num)
    return 0

virus(1)

total = 0

for i in range(N):
    if virus_list[i] == 1:
        total += 1

print(total-1)