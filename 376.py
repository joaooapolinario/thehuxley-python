livros = int(input())
alunos = int(input())
alu_livro = alunos / livros
if alu_livro >= 1 and alu_livro <= 8:
    print('A')
elif alu_livro >= 9 and alu_livro <= 12:
    print('B')
elif alu_livro >= 13 and alu_livro <= 18:
    print('C')
else:
    print('D')