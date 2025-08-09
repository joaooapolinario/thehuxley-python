dias = int(input())
km = int(input())

cota_km = 100*dias
if km > cota_km:
    print(f'{dias*90 + (km-cota_km)*12:.2f}')
else:
    print(f'{dias*90:.2f}')