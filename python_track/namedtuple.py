from collections import namedtuple
n = int(input())
data= namedtuple('data', input().split())
total = 0
for i in range(n):
    total += int(data(*input().split()).MARKS)
print(total/n)
