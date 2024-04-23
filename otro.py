##Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 0.04
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 1326,66 255,55  4546,54  


deposito = int(input('Ingrese la cantidad depositada'))
intereses = 0.04
year1 = deposito - (deposito * intereses)
year2 = year1 - (deposito * intereses)
year3 = year2 - (deposito * intereses)

print(f'Deposito: {deposito} \n Year1: {year1} \n Year2: {year2} \n Year3: {year3}')
