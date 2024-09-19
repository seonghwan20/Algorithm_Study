N = int(input())

size = list(map(int, input().split(' ')))

T, P =map(int, input().split(' '))

def order(s, num):
    if s%num == 0:
        return s//num
    else:
        return s//num + 1
    
num_T = 0 

for i in size:
    A = order(i, T)
    num_T = num_T + A
    
print(num_T)
print(sum(size)//P, end = ' ')
print(sum(size)%P)
