numeros = {}

n = int(input())

for i in range(n):
    linha = input().split()
    for j in linha:
        numeros[i] = [int(k) for k in linha]

somas_x = []
somas_y = []
somas_diag = []

for i in range(n):
    somas_x.append(sum(numeros[i]))

soma = 0
for j in range(n):
    for k in range(n):
        soma = numeros[k][j] + soma
    somas_y.append(soma)
    soma = 0
    
sum_diag1 = 0
for l in range(n):
    sum_diag1 = numeros[l][l] + sum_diag1
somas_diag.append(sum_diag1)

sum_diag2 = 0
index = 0
for k in range(n-1, -1, -1):
    sum_diag2 = numeros[k][index] + sum_diag2
    index +=1
    
   
somas_diag.append(sum_diag2)

if all(x == somas_x[0] for x in somas_x) and all(y == somas_y[0] for y in somas_y) and all(d == somas_diag[0] for d in somas_diag):
    print(somas_x[0])
else:
    print(-1)
