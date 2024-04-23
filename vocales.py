"""
Escribe un programa que tome una cadena de texto como entrada y devuelva el número de palabras de ese texto.
"""


texto = input('ingrese un texto\n')
contador = 0

for char in texto:
    if char == ' ':
        contador += 1
            
if len(texto) > 0:
    contador += 1
    
print(contador) 


