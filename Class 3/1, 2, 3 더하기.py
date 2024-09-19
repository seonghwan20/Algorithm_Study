import sys

input = sys.stdin.readline

T = int(input())

arr = [0 for i in range(10)]

arr[0] = 1
arr[1] = 2
arr[2] = 4

for i in range(3, 10):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    
for i in range(T):
    print(arr[int(input())-1])