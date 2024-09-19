N = int(input())

if N==1:
    print(0)
else:
    for i in range(1,N,1):
        sum_stri = 0
        for j in range(len(str(i))):
            sum_stri = sum_stri + int(str(i)[j])
        if i + sum_stri == N:
            print(i)
            break
        else:
            if i==N-1 :
                print(0)
                break
            else:
                continue