while True:
    N = int(input())
    if N == 0:
        break
    N = list(str(N))
    
    M = []
    for i in range(len(N)-1, -1, -1):
        M.append(N[i])
    
    for i in range(len(N)):
        if N[i] == M[i]:
            if i == len(N) - 1:
                print('yes')
                break
            else:
                continue
        else:
            print('no')
            break