quant_part = int(input())

part = {}

for i in range(quant_part):
    nome, p1, p2, p3 = input().split()
    part[nome] = [p1, p2, p3]


while True:
    presente = input().strip()
    
    if presente == 'FIM':
        break
    
    nome, presente = presente.split()
    
    if presente in part[nome]:
        print('Uhul! Seu amigo secreto vai adorar')
    else:
        print('Tente Novamente!')