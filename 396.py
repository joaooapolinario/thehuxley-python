quant_casa = 0
qt = 0
while True:
    quant = int(input())
    if quant == 999:
        break
    else:
        if quant > 2:
            qt += (quant-2)*12.89
            quant_casa += 1
        else:
            pass
            
print(f'{qt:.2f}')
print(quant_casa)