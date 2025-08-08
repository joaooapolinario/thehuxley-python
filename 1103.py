idade = int(input())
tipo = input().lower()

jogos = {
    'azar' : 21,
    'mmorpg' : 14, 
    'moba' : 10,
    'casual' : 0
}

if idade < 0 or idade > 130:
    print('Idade invalida.')
elif tipo not in jogos:
    print('Jogo invalido.')
elif idade >= jogos[tipo]:
    print('Pode entrar!')
else:
    print('Volte daqui há alguns anos.')
    