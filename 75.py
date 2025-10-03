voos = {}

for i in range(37):
    voo, lugares = map(int, input().split())
    voos[voo] = lugares

while True:
    pedidos = input()
    
    if pedidos == '9999':
        break
    
    id, voo_desej = map(int, pedidos.split())
    
    if voos.get(voo_desej) == None or voos[voo_desej] == 0:
        print('INDISPONIVEL')
    else:
        voos[voo_desej] -= 1
        print(id)

    