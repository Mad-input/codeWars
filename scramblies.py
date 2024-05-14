"""
Completa la función scramble(str1, str2) que devuelve true si una porción de str1 los personajes se pueden reorganizar para que coincidan str2, de lo contrario regresa false.

Notas:

Solo se utilizarán letras minúsculas ( a-z ). No se incluirán signos de puntuación ni dígitos.
El rendimiento debe ser considerado.

Ejemplos
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True

print(sorted(set("abcdef")))