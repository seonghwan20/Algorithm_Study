T = int(input())

i = 0

while(i<T):
    arr = input()
    score = list(range(0, len(arr), 1))
    for j in range(len(arr)):
        if j == 0:
            if arr[j] == 'O':
                score[j] = 1;
            else:
                score[j] = 0;
        else:
            if arr[j] == 'O':
                score[j] = score[j-1] + 1
            elif arr[j] == 'X':
                score[j] = 0
    print(sum(score))
    i = i + 1