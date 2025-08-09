salario = float(input())
bonus = (75/100)*salario

if bonus < 2000:
    print('ARGENTINA')
elif bonus >= 2000 and bonus <= 3000:
    print('ESPANHA')
else:
    print('ALEMANHA')