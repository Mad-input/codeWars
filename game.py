import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Definir tamaño de pantalla
ANCHO = 600
ALTO = 400

# Definir tamaño de celda y margen
TAMANO_CELDA = 20
MARGEN = 1

# Definir laberinto
laberinto = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X..............X..X",
    "X..XXXXXXX.XXX.X..X",
    "X....X....X...X...X",
    "X....X....X...X...X",
    "X....X....X...X...X",
    "X..........X...X...X",
    "XXXXXXXXXXXXXXXXXX.X",
    "X..............X...X",
    "X..............X...X",
    "XXXXXXXXXXXXXXXXXXXX"
]

# Posición inicial del jugador
jugador_x = 1
jugador_y = 1

# Inicializar ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto")

# Función para dibujar laberinto
def dibujar_laberinto():
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            color = BLANCO if laberinto[fila][columna] == "X" else NEGRO
            pygame.draw.rect(pantalla, color, [(MARGEN + TAMANO_CELDA) * columna + MARGEN,
                                                (MARGEN + TAMANO_CELDA) * fila + MARGEN,
                                                TAMANO_CELDA, TAMANO_CELDA])

# Función para dibujar jugador
def dibujar_jugador():
    pygame.draw.rect(pantalla, ROJO, [(MARGEN + TAMANO_CELDA) * jugador_x + MARGEN,
                                       (MARGEN + TAMANO_CELDA) * jugador_y + MARGEN,
                                       TAMANO_CELDA, TAMANO_CELDA])

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if jugador_y > 0 and laberinto[jugador_y - 1][jugador_x] != "X":
                    jugador_y -= 1
            elif evento.key == pygame.K_DOWN:
                if jugador_y < len(laberinto) - 1 and laberinto[jugador_y + 1][jugador_x] != "X":
                    jugador_y += 1
            elif evento.key == pygame.K_LEFT:
                if jugador_x > 0 and laberinto[jugador_y][jugador_x - 1] != "X":
                    jugador_x -= 1
            elif evento.key == pygame.K_RIGHT:
                if jugador_x < len(laberinto[0]) - 1 and laberinto[jugador_y][jugador_x + 1] != "X":
                    jugador_x += 1
    
    # Limpiar pantalla
    pantalla.fill(NEGRO)
    
    # Dibujar laberinto
    dibujar_laberinto()
    
    # Dibujar jugador
    dibujar_jugador()
    
    # Actualizar pantalla
    pygame.display.flip()
