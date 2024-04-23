#Un isograma es una palabra que no tiene letras repetidas, consecutivas o no consecutivas. 
# Implemente una función que determine si una cadena que contiene solo letras es un isograma. 
# Suponga que la cadena vacía es un isograma. Ignorar mayúsculas y minúsculas.

#Ejemplo: (Entrada --> Salida)

#"Dermatoglifos" --> verdadero "aba" --> falso "moOse" --> falso (ignorar mayúsculas y minúsculas)

#"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram('Dermatoglyphics'))