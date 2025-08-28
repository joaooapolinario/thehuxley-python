menor_matri = 0
menor_cre = 99999
soma = 0
quant = 0
while True:
    matri = int(input())
    if matri == 999:
        break
    cre = float(input())
    if cre < menor_cre:
        menor_cre = cre
        menor_matri = matri
    soma += cre
    quant += 1

print(menor_matri)
print(f'{soma/quant:.2f}')