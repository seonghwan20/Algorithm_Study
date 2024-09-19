import sys
import math

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

num_list = [0]*8001
sorted_list = []

def round(num):
    if num - math.floor(num) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)
    
def most(list):
    most_num = list.index(max(list))
    try:
        if list.index(max(list), most_num+1, 8001):
          most_num = list.index(max(list), most_num+1, 8001)
          return most_num - 4000
    except:
        return most_num - 4000

for i in range(N):
    n = int(input())
    num_list[n+4000] += 1
    sorted_list.append(n)
    
sorted_list.sort()

print(str(round(sum(sorted_list)/N)) + '\n')
print(str(sorted_list[int((N-1)/2)]) + '\n')
print(str(most(num_list)) + '\n')
print(str(sorted_list[N-1] - sorted_list[0]))