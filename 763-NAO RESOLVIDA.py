# NAO RESOLVIDA !!
nome = input().strip().replace(" ", "").lower()

palindromo = nome[::-1]

if nome == palindromo:
    print("SIM")
    print(len(nome) // 2)
else:
    print("NAO")
