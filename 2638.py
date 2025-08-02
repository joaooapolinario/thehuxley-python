acd = float(input('Digite o pH da solucao:\n'))
if acd >=0 and acd <= 14:    
    if acd < 7.0:
        print('Essa solucao e acida.')
    elif acd > 7.0:
        print('Essa solucao e basica.')
    else:
        print('Essa solucao e neutra.')
else:
    print('Valor deve estar entre 0 e 14.')
        