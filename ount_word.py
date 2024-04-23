# 4. Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.

def nums_words (phrase):
    return f'Tiene {len(phrase.split(' '))} palabras'

phrase = input('Ingrese una frase: ')
print(nums_words(phrase))