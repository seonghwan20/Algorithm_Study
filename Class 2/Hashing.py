r = 31

M = 1234567891

L = int(input())
hash = list(input())

alpha = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sum = 0

for i in range(len(hash)):
    idx = alpha.index(hash[i]) #ord 를 사용하면 편하다 (아스키코드로 변환)
    sum += idx*(r**i)
  
print(sum%M)