A = input()
B = input()
C = input()

arr = [A, B, C]

for i in arr:
    try:
        i = int(i)
        if str(i) == A:
            i += 3
        elif str(i) == B:
            i += 2
        elif str(i) == C:
            i += 1
        if (i%3 == 0 and i%5 == 0):
            print('FizzBuzz')
            break
        elif (i%3 == 0 and i%5 != 0):
            print('Fizz')
            break
        elif (i%3 != 0 and i%5 == 0):
            print('Buzz')
            break
        else:
            print(i)
            break
    except:
        continue
