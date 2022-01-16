import re
n = input();

for i in range(int(n)):
    t = input();
    try:
        re.compile(t)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid);
