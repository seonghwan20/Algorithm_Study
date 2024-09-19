T = int(input())

weight = []
height = []
rank = []

for i in range(T):
    w, h = map(int, input().split(' '))
    weight.append(w)
    height.append(h)

for i in range(T): #랭크 배열에 랭크 추가
    r = 1
    for j in range(T): # 몸무게 순위 정하기
        if i == j:
            continue
        if weight[i] < weight[j] and height[i] < height[j]:
            r += 1
    rank.append(r)

for _ in rank:
    print(_, end=' ')