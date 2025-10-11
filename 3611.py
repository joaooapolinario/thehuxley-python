
contatos = []
vinculos = {1:'Familia', 2 :'Faculdade', 3:'Amigo'}
n = int(input())

for _ in range(n):
    nome = input()
    numero = input()
    vinculo = int(input())
    contatos.append({'nome': nome, 'numero': numero, 'vinculo': vinculo})

while True:
    pesquisa = input()
    if pesquisa == '#':
        break
    
    encontrados = [c for c in contatos if c['nome'].startswith(pesquisa + '') or c['nome'] == pesquisa]
    
    if not encontrados:
        print(f'{pesquisa} nao foi cadastrado\n')
    else:
        for contato in encontrados:
            print(f'Nome: {contato["nome"]}')
            print(f'Numero: {contato["numero"]}')
            print(f'Vinculo: {vinculos[contato["vinculo"]]}\n')
            

