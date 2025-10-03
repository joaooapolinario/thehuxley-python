n = int(input())

bois = {}

for i in range(n):
    boi = input().split()
    bois[boi[0]]= float(boi[1])
    
gordo = max(bois.values())
id_gordo = 0
magro = min(bois.values())
id_magro = 0
for key, val in bois.items():
    if val == gordo:
        id_gordo = key
    elif val == magro:
        id_magro = key

print(f'Gordo: id: {id_gordo} peso: {gordo:.2f}Kg')
print(f'Magro: id: {id_magro} peso: {magro:.2f}Kg')
