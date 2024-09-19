import math

num = int(input())

if (num - math.floor(num)) >= 0.5:
    num = math.ceil(num)
else:
    num = math.floor(num)
    
print(num)