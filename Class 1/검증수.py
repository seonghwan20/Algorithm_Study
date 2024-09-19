arr = list(map(int, input().split(' ')))

num = 0

for i in arr:
    num = num + i*i

print(num%10)