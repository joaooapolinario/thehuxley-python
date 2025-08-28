limite = int(input())
cont = []
for i in range(1, limite + 1):
    soma = 0
    for j in range(i, 0, -1):   
        if i % j == 0:
            soma += j
           
    if soma == i*2:
        cont.append(i)
for i in cont:
    print(i)
    