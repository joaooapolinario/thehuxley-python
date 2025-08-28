n1 = int(input())
n2 = int(input())

cont = 0
for i in range(1, 50):
    if i % n1 == 0 and i % n2 == 0:
        cont += 1
        
print(cont)