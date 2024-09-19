import sys

input = sys.stdin.readline
while True:
    arr = []
    temp = list(input().rstrip())
    if len(temp) == 1 and temp[0] == '.':
        break
    for j in temp:
        if j=='(' or j==')' or j=='[' or j==']':
            arr.append(j)
    while True:
        if len(arr) == 0:
            print('yes')
            break
        change = False
        i = 0
        while i < len(arr) - 1:
            if arr[i] == '(' and arr[i+1] == ')':
                del arr[i]
                del arr[i]
                change = True
                i += 1
                continue
            if arr[i]  == '[' and arr[i+1] == ']':
                del arr[i]
                del arr[i]
                change = True
                i += 1
                continue
            i += 1
        if change:
            continue
        else:
            print('no')
            break