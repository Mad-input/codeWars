year = int(input('Ingrese un año: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('es bisiesto')
else:
    print('no es bisiesto') 