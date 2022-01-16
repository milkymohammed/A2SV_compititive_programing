n = input()
l = []
u = []
o = []
e = []
for i in n:
    if i.islower():
        l.append(i)
    elif i.isupper():
        u.append(i)
    elif i.isdigit():
        if int(i)%2 == 0:
            e.append(i)
        elif int(i)%2 != 0:
            o.append(i)
a =sorted(l)+sorted(u)+sorted(o)+sorted(e)
for i in a:
    print(i,end = "")
