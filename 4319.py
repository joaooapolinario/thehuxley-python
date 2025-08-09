'''
Escreva um programa para verificar se um aluno está ou não aprovado.

São realizadas 03 provas (prova 1, prova 2 e prova de reposição). Todos os alunos são obrigados a fazer todas as provas.

Caso o aluno seja maior de idade, a média final é calculada com a média ponderada entre média aritmética das provas 1 e 2 (peso 6) e a nota da prova de reposição (peso 3).

Caso o aluno seja menor de idade, a nota da prova de reposição só será considerada caso a nota da prova 1 ou prova 2 for menor do que 7. Nesse caso (alguma das notas da prova 1 e 2 forem menor do que 7), a média final será a média aritmética das duas maiores notas. Caso contrário, a média final será a média aritmética das provas 1 e 2.

O aluno será considerado aprovado quando a média final for igual ou maior que 5.5. Entretanto, há um requisito adicional, o aluno não pode ter nenhuma nota abaixo de 4.0. Caso contrário, será reprovado.

Se o aluno estiver aprovado, o programa deve exibir a mensagem: "Aprovado". Caso contrário, deve exibir a mensagem: "Reprovado".
'''



idade = int(input())
n1 = float(input())
n2 = float(input())
rep = float(input())

if idade >=18:
    mf = (((n1+n2)/2)*6 + rep*3)/9
    if mf >= 5.5 and n1 >= 4 and n2 >= 4 and rep >= 4:
        print('Aprovado')
    else:
        print('Reprovado')
    
else:
    if n1 >= 7 or n2 >= 7:
        mf = (n1+n2)/2 
        if mf >= 5.5 and n1 >= 4 and n2 >= 4:
            print('Aprovado')
        else:
            print('Reprovado')
    else:
        menor = min(n1, n2)
        maior = max(n1, n2)
        if menor < 7:
            menor = rep
            mf = (maior + menor)/2
            if mf >= 5.5 and n1 >= 4 and n2 >= 4:
                print('Aprovado')
            else:
                print('Reprovado')