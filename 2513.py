'''
para que três segmentos de reta com medidas a, b e c formem um triângulo,
as seguintes desigualdades devem ser verdadeiras:
a + b > c,
a + c > b,
b + c > a.
'''
a = int(input())
b = int(input())
c = int(input())

if  a + b > c and a + c > b and b + c > a:
    print('sim')   
else:
    print('nao')