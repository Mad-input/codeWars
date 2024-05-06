"""
Pregunte al usuario cuántos elementos desea ingresar en una lista, 
luego solicite cada uno de ellos y presente el contenido de la lista y su contenido invertido.

"""


lenList = int(input('Cuántos elementos quiere agregar a la lista?: '))
lista = list()

while lenList > 0:
    elem = input('Elemento: ')
    lista.append(elem)
    lenList -= 1

print(f'Contenido: {' - '.join(lista)} Contenido invertido: {' - '.join(lista)[::-1]}')








# #* 2. Crear una lista de números y solicitar un número.  Borrar de la lista ese número en todas las posiciones donde se encuentre.  
# #* Presentar la lista final

# lista = [1,2,3,4,5,6,7,8,2,1,3,4]
# res = int(input('Introdusca un numero: '))

        
# print([x for x in lista if x != res])
    


    
    
 
 
 
    
    
"""
3. Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas listas

ejemplo:
frase1:  "holasena"
frase2:  "todogana"
salida: ["o","n", "a"]
"""

# frase1 = input('Ingrese la primera frase: ')
# frase2 = input('Ingrese la segunda frase: ')
# listaReps = []

# ## Hola
# ## Como

# for c1, c2 in zip(frase1,frase2):
#     if c1 == c2:
#         listaReps.append(c1)
        
# print(f"""
#       Frase 1: {frase1}
#       Frase 2: {frase2}
#       Letras repetidas: {listaReps}
#       """)
