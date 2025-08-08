peso = float(input())
if peso <= 20 and peso > 0:
    print(f'{0.0:.2f}')
elif peso > 20 and peso <= 25:
    taxa = (peso - 20) * 12.50
    print(f'{taxa:.2f}')
elif peso > 25 and peso <= 30:
    taxa = (peso - 20) * 32.75
    print(f'{taxa:.2f}')
else:
    print('PESO LIMITE EXCEDIDO')