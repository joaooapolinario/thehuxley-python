quant = 0
while True:
    quant_prego = int(input())
    if quant_prego % 2 != 0:
        break
    quant += quant_prego

if quant % 12 == 0:
    total = quant // 12 * 7.89
    print(f'{total:.2f}')
    print(0)
else:
    total = (quant // 12 * 7.89) + 7.89
    print(f'{total:.2f}')
    print(12 - (quant % 12))
    

    