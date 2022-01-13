from itertools import permutations
word,number = (input().split(' '))
for i in list(permutations(sorted(word),int(number))):
    print(''.join(i))
