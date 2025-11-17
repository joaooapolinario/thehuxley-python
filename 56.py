p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
ambos = []

for matricula in p2:
    if matricula in p3:
        ambos.append(matricula)
for i in ambos:
    print(i, end=' ')