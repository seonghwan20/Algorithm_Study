import sys
input = sys.stdin.readline

calculate_line = list(map(str, input().rstrip().split('-')))

for i in range(len(calculate_line)):
    temp = list(map(int, calculate_line[i].split('+')))
    calculate_line[i] = sum(temp)
    
print(calculate_line[0] - sum(calculate_line[1:]))