n,m=input().split()
m=int(m)
l=[]
for i in range(m):
    no=list(map(float,input().split()))
    l.append(no)
    
for i in zip(*l):
    print(sum(i)/m)
