x = int(input())
numeros = []
maximo = 0
while maximo < 20:
    maximo +=1
    n = int(input())    
    if n == -1:
        break
    
    numeros.append(n)

contagem = numeros.count(x)
soma = 0
cont = 0
for i in numeros:
    if (i > 0 and i < 15) or i > 20:
        soma += i
        cont += 1

print(f'O número {x} apareceu {contagem} vez(es)')
if cont == 0:
    print('Sem valores para calcular a média')
else:         
    print(f'A média dos números foi de: {soma/cont:.2f}')




