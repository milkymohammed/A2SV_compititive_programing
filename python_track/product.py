from itertools import product
M  = list(map(int,input().split()))
N  = list(map(int,input().split()))
print (*list(product(M,N)))
