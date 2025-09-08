gab = input()
cont = 0
cont_aprov = 0
notas = []

while True:
    resp = input()
    if resp == '9999':
        break
    cont += 1
    n, r = resp.split()
    nota = 0
    for i in range(len(gab)):
        if gab[i] == r[i]:
            nota += 1
    notas.append(nota)
    if nota >= 6:
        cont_aprov += 1
    
    print(f'{n} {nota:.1f}')
    
porcent_aprov = (cont_aprov/cont)*100
print(f'{porcent_aprov:.1f}%')
frequencia_notas = {}
for j in notas:
    frequencia_notas[j] = frequencia_notas.get(j, 0) + 1

nota_mais_frequente = max(frequencia_notas, key=frequencia_notas.get)
print(f'{nota_mais_frequente:.1f}')

