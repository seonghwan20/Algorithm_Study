import sys

input = sys.stdin.readline

t = int(input())



for _ in range(t):
    subject_list = []
    num = []
    n = int(input())
    for i in range(n):
        name, subject = map(str, input().rstrip().split(' '))
        if subject not in subject_list:
            subject_list.append(subject)
            num.append(1)
        else:
            num[subject_list.index(subject)] += 1
    total = 1
    for i in range(len(num)):
        total *= num[i]+1
    print(total-1)