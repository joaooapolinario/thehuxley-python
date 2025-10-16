'''
P = M * A
'''
gravidade_planetas = {
    'sol': 273.42,
    'mercurio' : 3.78,
    'venus' : 8.6,
    'terra' : 9.8,
    'marte' : 3.72,
    'jupiter' : 24.8,
    'saturno' : 10.5,
    'urano' : 8.5,
    'netuno' : 10.8,
    'plutao' : 5.88,
    'lua' : 1.67
}

peso_terra = float(input())
massa = peso_terra / gravidade_planetas['terra']

for i in gravidade_planetas:
    print(f'{massa * gravidade_planetas[i]:.2f}')