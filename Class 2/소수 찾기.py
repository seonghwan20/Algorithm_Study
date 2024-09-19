N = int(input())

num_list = list(map(int, input().split(' ')))

prime = 0

def prove(num):
    for i in range(2,num,1):
        if num%i==0:
            return False
    return True

for i in num_list:
    if i == 1:
        continue
    if prove(i):
        prime = prime + 1
    else:
        continue
    
print(prime)
        