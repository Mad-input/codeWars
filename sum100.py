##Problema de la contraseña:

#Crea una función que valide contraseñas. La contraseña debe tener al menos 8 caracteres, 
# contener al menos una letra mayúscula, una letra minúscula y un número.

def validar_contrasena(contrasena):
    # Verificar la longitud de la contraseña
    if len(contrasena) < 8:
        return False

    # Verificar si hay al menos una letra mayúscula
    if not any(c.isupper() for c in contrasena):
        return False

    # Verificar si hay al menos una letra minúscula
    if not any(c.islower() for c in contrasena):
        return False

    # Verificar si hay al menos un número
    if not any(c.isdigit() for c in contrasena):
        return False

    # La contraseña cumple con todos los criterios
    return True



