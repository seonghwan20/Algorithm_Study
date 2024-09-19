T = int(input())

i = 0

def A(num):
    if num<10 :
        num = str(0) + str(num)
    else:
        num = str(num)
while(i < T):
    H, W, N = map(int, input().split(' '))
    a = N%H
    if (a==0):
        b = N//H
        if b<10:
            b = str(0) + str(b)
        else:
            str(b)
        if H<10:
            H = str(0) + str(H)
        else:
            str(H)
        a = H
    else:
        if a<10:
            a = str(0) + str(a)
        else:
            str(a)
        b = N//H + 1
        if b<10:
            b = str(0) + str(b)
        else:
            str(b)
    print(int(str(a)+str(b)))
    i = i + 1



