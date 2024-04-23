# 5. Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

def reverse_phrase(phrase):
    return phrase.upper()[::-1]

phrase = input('Ingrese Una frase: ')
print(reverse_phrase(phrase))