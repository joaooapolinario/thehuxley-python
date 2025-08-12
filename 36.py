m = int(input())
n = int(input())
aux = 1
maximo = 0
while True:
    if m * aux <= n:
        maximo = m * aux
        aux += 1
    else:
        break
    
if maximo == 0:
    print(f'sem multiplos menores que {n}')
else:
    print(maximo)