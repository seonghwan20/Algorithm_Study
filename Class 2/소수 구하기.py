import sys

input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split(' '))

sieve = [False, False] + [True] * (N-1)
primes = []
for i in range(2, N+1):
    if sieve[i]:
        primes.append(i)
        for j in range(i*2, N+1, i):
            sieve[j] = False
for i in range(len(primes)):
    if primes[i]:
        if primes[i] >= M and primes[i] <= N:
            print(str(primes[i]) + '\n')
    
    