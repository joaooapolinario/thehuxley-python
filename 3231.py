n = int(input())
if n % 5 == 0:
    print('nao')
elif n % 4 == 0 and n % 7 == 0:
    print('sim')
else:
    print('nao')