preco = {1 : 5.30, 2 : 6.00, 3 : 3.20, 4: 2.50}

cod = int(input())
quant = int(input())
val = preco[cod] * quant
if quant >= 15 or val >= 40:
    val_final = val - (15/100)*val
else:
    val_final = val
print(f'R$ {val_final:.2f}')
