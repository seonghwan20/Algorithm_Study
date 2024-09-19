import sys

input = sys.stdin.readline

T = int(input())

fibonacci_0 = [0]*41
fibonacci_1 = [0]*41

fibonacci_0[0] = 1
fibonacci_0[1] = 0

fibonacci_1[0] = 0
fibonacci_1[1] = 1

for i in range(2,41):
    fibonacci_0[i] = fibonacci_0[i-2] + fibonacci_0[i-1]
    fibonacci_1[i] = fibonacci_1[i-2] + fibonacci_1[i-1]
for i in range(T):
    idx = int(input())
    print(fibonacci_0[idx], fibonacci_1[idx], sep=' ')
    