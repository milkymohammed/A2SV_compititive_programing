from collections import OrderedDict
n = int(input())
itemprice = OrderedDict()
for i in range(0,n):
    *item, price = input().split()
    LEN,r = len(item), " ".join(item)
    if r not in itemprice:
        itemprice[r] = int(price)
    else:
        itemprice[r] +=int(price)
[print(itemprices,itemprice[itemprices]) for itemprices in itemprice]
