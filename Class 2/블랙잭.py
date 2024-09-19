N, M =map(int, input().split(' '))
num_list = list(map(int, input().split()))

min = M
sum = 0

for i in range(0, len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for k in range(j+1, len(num_list)):
            sub = M - (num_list[i]+num_list[j]+num_list[k])
            if sub < 0:
                continue
            elif min > sub:
                min = sub
                sum = num_list[i]+num_list[j]+num_list[k]
            else:
                continue
            
print(sum)