# 1. Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.

# Fórmula:
# Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100%


def indice_de_cosecha (frutos_prod, frutos_rec):
    return (frutos_rec / frutos_prod) * 100

frutos_prod = 500
frutos_rec = 200
print(f'El índice de cosecha es {indice_de_cosecha(frutos_prod, frutos_rec)}%')  