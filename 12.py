card = {}
val_pagar = 0


n = int(input())

for i in range(n):
    cod = int(input())
    nome = input()
    preco = float(input())
    card[cod] = [nome, preco]
    
while True:
    cod = int(input())
    if cod == 0:
        break
    quant = int(input())
    
    
    if cod not in card or quant < 1:
        val_pagar +=0
    else:
        val_pagar += card[cod][1] * quant
print(f'{val_pagar:.2f}')