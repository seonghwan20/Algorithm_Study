import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    arr = [0]*n
    arr[0] = 1
    arr[1] = 2  
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[-1]%10007)
    
