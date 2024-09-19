import math

N, K = map(int, input().split(' '))

print(int(int(math.factorial(N))/(int(math.factorial(K))*int(math.factorial(N-K)))))
