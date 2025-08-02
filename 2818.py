acd = float(input('Digite o pH da solucao:\n'))
if acd >=0 and acd <= 14:    
    if acd < 7.0:
        print('Solucao acida')
    elif acd > 7.0:
        print('Solucao basica')
    else:
        print('Solucao neutra')
else:
    print('Valor do pH deve estar entre 0 e 14')