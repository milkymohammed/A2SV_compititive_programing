import collections 
from collections import Counter
noshoes = int(input())
listofshoes = collections.Counter(map(int,input().split(' ')))
costumers = int(input())
sizeshoes = Counter(listofshoes).keys()
noshoes = Counter(listofshoes).values() 
income = 0
for i in range(costumers):
    size,price = map(int,input().split(' '))
    if listofshoes[size]: 
            income += price
            listofshoes[size] -= 1

print (income)
