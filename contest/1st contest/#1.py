a.

n = 4
for i in range(n): 
    print (' ', end = " ")
    for j in range(i,n-1):
        print (' ', end = " ")
    for k in range(i+1):
        print ('*', end = " ")
    for k in range(i):
        print ('*', end = " ")
    print()

    
    
   b.
  
n = 4
for i in range(n): 
    print ('*', end = " ")
    for j in range(i):
        print ('*', end = " ")
    print()
