N, numbers=int(input()), list(map(int, input().split()))
print(any([str(i)==str(i)[::-1] for i in numbers]) and all([i>0 for i in numbers]))
