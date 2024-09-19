N, M = map(int, input().split(' '))

if N > M:
    A = N
    B = M
else:
    A = M
    B = N

r = []

if A%B == 0:
    gcd = B
else:
    r.append(A%B)
    if B%r[0] == 0:
        gcd = r[0]
    else:
        r.append(B%r[0])
        i = 2
        while True:
            if r[i-2]%r[i-1] == 0:
                gcd =r[i-1]
                break
            else:
                r.append(r[i-2]%r[i-1])
                i += 1

if gcd == 0:
    lcm = N*M
else:
    lcm = abs(N*M)/gcd

print(gcd)
print(int(lcm))