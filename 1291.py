soma = 0
soma_diag = 0
maior = None

for i in range(3):
    for j in range(3):
        n = int(input())
        soma += n
        if maior is None or n > maior:
            maior = n
        if i == j: 
            soma_diag += n

media = soma / 9

if maior > 0:
    delta = 1
elif maior == 0:
    delta = 0
else:
    delta = -1

print(f"{media:.2f} {maior} {delta} {soma_diag}")