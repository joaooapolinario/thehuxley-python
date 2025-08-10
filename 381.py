aux = 0
cont = 0
while True:
    n = int(input())
    aux += n
    if aux > 18:
        break
    cont += 1
print(cont)