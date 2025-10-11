nome = input().replace(" ", "").lower()

palindromo = nome[::-1]

if nome == palindromo:
    print("SIM")
    print((len(nome) + 1) // 2)
else:
    print("NAO")
