import sys

input = sys.stdin.readline

N = int(input())

times = [0]*(10**6+1)

times[1], times[2], times[3] = 0, 1, 1

for i in range(4,N+1):
    if i%6 == 0 :
        times[i] = min(times[i//2], times[i//3]) + 1
    elif i%3 == 0:
        times[i] = min(times[i//3], times[i-1]) + 1
    elif i%2 == 0:
        times[i] = min(times[i//2], times[i-1]) + 1
    else:
        times[i] = times[i-1] + 1
        
print(times[N])