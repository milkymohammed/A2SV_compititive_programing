n = 4
for i in range(n): 
    print ('*', end = " ")
    for j in range(i):
        print ('*', end = " ")
    for k in range(i,n-1):
        print (' ', end = " ")
    for l in range(i,n-1):
        print (' ', end = " ")
    for j in range(i+1):
        print ('*', end = " ")
    print()
