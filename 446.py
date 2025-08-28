quant = int(input())
aux = 0
for i in range(quant):
    aux += 1
    if aux % 3 == 0:
        quant -= 1
print(f'{quant * 2.20:.2f}')
