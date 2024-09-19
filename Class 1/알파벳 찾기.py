word = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in alpha:
    if i not in word:
        print('-1', end = ' ')
    elif i in word:
        for j in range(len(word)):
            if i == word[j]:
                print(j, end=' ')
                break;