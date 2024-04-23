def vocal():
    letter = input('Ingrese una letra: ')
    if len(letter) > 1:
        print('solo una letra')
    else:
        if not letter in 'aeiou':
            print('No es una vocal')
        else: print('es una vocal')
vocal()
