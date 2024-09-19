import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

pok_list = []

class Pokemon:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def __repr__(self):
        return repr((self.name, self.num))
num = 1
for i in range(N):
    pok_list.append(Pokemon(input().rstrip(), num))
    num += 1

    
new_pok_list = sorted(pok_list, key = lambda pokemon: pokemon.name)

def binary_search(list, pok_name, low, high):
    if low <= high:
        middle = (low+high)//2
        if list[middle].name == pok_name:
            return list[middle].num
        elif list[middle].name < pok_name:
            return binary_search(list, pok_name, middle+1, high)
        elif list[middle].name > pok_name:
            return binary_search(list, pok_name, low, middle-1)

for i in range(M):
    pok_name = input().rstrip()
    if pok_name[0].isalpha():
        print(binary_search(new_pok_list, pok_name, 0, N-1))
    else:
        print(pok_list[int(pok_name)-1].name)