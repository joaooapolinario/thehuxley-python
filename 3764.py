while True:
    acd = float(input('')) 
    if acd == -1:
        break
    if acd < 7.0:
        print('ACIDA')
    elif acd > 7.0:
        print('BASICA')
    else:
        print('NEUTRA')