n = int(input())
if n >= 5 and n <= 7:
    print('Infantil A')
elif n >= 8 and n <= 10:
    print('Infantil B')
elif n >= 11 and n <= 13:
    print('Juvenil A')
elif n >= 14 and n <= 17:
    print('Juvenil B')
elif n >= 18 and n <= 40:
    print('Adulto')   
elif n > 40:
    print('Master')
else:
    print('Idade invalida.') 
    
    