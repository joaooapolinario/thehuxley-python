salario = float(input())
comprometido = float(input())

limite_livre = (salario * (30/100)) - comprometido
if limite_livre >0:   
    print(f'{limite_livre:.2f}')
else:
    print(f'{0.0:.2f}')