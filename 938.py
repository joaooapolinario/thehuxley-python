a = 0
for i in range(5):
    n = float(input('Digite um valor:\n'))
    if n < 0:
        a +=1
    else:
        pass
    
print('Foram digitados',a,'numeros negativos')