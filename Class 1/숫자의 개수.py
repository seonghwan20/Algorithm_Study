A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

for i in range(10):
    print(result.count(str(i)))
    
#
for i in range(0,10,1):
    a = 0
    for j in result:
        if i == int(j):
            a = a + 1
        else:
            continue
    print(a)
#