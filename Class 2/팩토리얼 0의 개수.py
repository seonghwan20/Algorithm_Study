import math

N = int(input())

fact = list(str(math.factorial(N)))
i=0
j=-1
while True:
    if int(fact[j]) == 0:
        i+=1
    else:
        print(i)
        break
    j -= 1