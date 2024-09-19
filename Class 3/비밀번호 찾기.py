import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

temp = [ list(map(str, input().rstrip().replace('.', '').split(' '))) for i in range(N)]

site_list = sorted(temp, key = lambda site: site[0])

def bianry_search(list, key, low, high):
    if low <= high:
        middle = (low+high)//2
        if list[middle][0] == key:
            return list[middle][-1]
        elif list[middle][0] < key:
            return bianry_search(list, key, middle+1, high)
        elif list[middle][0] > key:
            return bianry_search(list, key, low, middle-1)
    else:
        return -1
        
for i in range(M):
    key = input().replace('.','').rstrip()
    print(bianry_search(site_list, key, 0, N-1))
