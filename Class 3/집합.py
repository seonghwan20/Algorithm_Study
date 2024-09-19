import sys

input = sys.stdin.readline
print = sys.stdout.write

M = int(input())

number = set()

for i in range(M):
    arr = list(map(str, input().rstrip().split(' ')))
    if arr[0] == 'add':
        number.add(arr[1])
    elif arr[0] == 'remove':
        number.discard(arr[1])
    elif arr[0] == 'check':
        if str(arr[1]) in number:
            print(str(1) + '\n')
        else:
            print(str(0) + '\n')
    elif arr[0] == 'toggle':
        if arr[1] in number:
            number.remove(arr[1])
        else:
            number.add(arr[1])
    elif arr[0] == 'all':
        number.clear()
        number.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif arr[0] == 'empty':
        number.clear()