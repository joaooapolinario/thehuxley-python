aux = 0
while True:
    pt = int(input())
    if pt < 0:
        break
    mt = int(input())
    red = float(input())
    if pt >= (50*(80/100)) and mt >= (35 * (60/100)) and red >= 7:
        aux += 1
print(aux)