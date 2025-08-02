a = 0
b = 0
c = 0
for i in range (3):
    n = int(input())
    if i == 0:
        a = n
    if i == 1:
        b = n
    else:
        c = n
if a == b == c:
    print('*')
if a == b != c:
    print('C')
if a == c != b:
    print('B')
if c == b != a:
    print('A')