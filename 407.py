def ciclo(n):
    cont = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cont += 1
    return cont


while True:
    try:
        i, j = map(int, input().split())
        a, b = i, j

        if i > j:
            i, j = j, i

        max_ciclo = 0
        for n in range(i, j + 1):
            tam = ciclo(n)
            if tam > max_ciclo:
                max_ciclo = tam

        print(a, b, max_ciclo)
    except:
        break
