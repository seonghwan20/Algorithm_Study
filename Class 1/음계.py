numlist = [1, 2, 3, 4, 5, 6, 7, 8]

m = list(map(int, input().split(' ')))

def a(arr):
    for i in range(8):
        if m[i] == numlist[i]:
            if i==7:
                return 'ascending'
            else:
                continue
        else:
            break
    for i in range(8):
        if m[i] == numlist[7-i]:
            if i==7:
                return 'descending'
            else:    
                continue
        else:
            break
    return 'mixed'
        
print(a(m))