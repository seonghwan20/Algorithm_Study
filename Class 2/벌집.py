N = int(input())

i = 2

def sum(num):
    total_sum = 0
    for i in range(1, num+1, 1):
        total_sum = total_sum + i
    return total_sum

while True:
    if N==1:
        print(1)
        break
    if (N-2)//6 == 0:
        print(2)
        break
    if (N-2)//6 < sum(i):
        print(i+1)
        break
    else:
        i = i+1
        continue