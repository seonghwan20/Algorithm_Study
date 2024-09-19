def tri(a, b, c):
    if a*a == b*b + c*c:
        print('right')
    else:
        print('wrong')

while True:    
    A, B, C = map(int, input().split(' '))
    if A==0 & B==0 & C==0:
        break
    if (A > B)&(A > C):
        tri(A,B,C)
    elif (B > C)&(B > A):
        tri(B,A,C)
    elif (C > A)&(C > B):
        tri(C,A,B)