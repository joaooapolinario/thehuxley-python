alunos = []

for i in range(100):
    nome = input()
    if nome == 'SAIR':
        break
    senha = int(input())
    situation = input().upper()
    alunos.append([nome, senha, situation])

while True:
    senha_aluno = int(input())
    if senha_aluno == -1:
        break
    found = False
    for aluno in alunos:
        if aluno[1] == senha_aluno:
            found = True
            if aluno[2] == 'P':
                print(f'{aluno[0]}, seja bem-vindo(a)!')
            else:
                print(f'Não está esquecendo de algo, {aluno[0]}? Procure a recepção!')
    if not found:
        print('Seja bem-vindo(a)! Procure a recepção!')