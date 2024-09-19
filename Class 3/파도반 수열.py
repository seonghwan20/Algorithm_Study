import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = [1, 1, 1, 2, 2]
    n = int(input())
    if n <= 5:
        print(arr[n-1])
    else:
        while len(arr) < n:
          arr.append(arr[-1] + arr[-5])
        print(arr[-1])