import pygame # Libreria para visualizar el código
import numpy as np # Libreria para datos y calculos
import time # libreria para usar el tiempo
import random # Libreria para poder iniciar el tablero pygame en una semilla aleatoria

pygame.init() # Iniciamos pygame

# Función para inicializar el tablero con una semilla aleatoria
def randomSeed(nxC, nyC, seedPorcent):
    seed = np.zeros((nxC, nyC))
    celulasVivas = int((seedPorcent / 100) * nxC * nyC)
    for _ in range(celulasVivas):
        x, y = random.randint(0, nxC-1), random.randint(0, nyC-1)
        seed[x, y] = 1
    return seed

# Función para contar vecinos vivos
def Neighbors(gameState, x, y, nxC, nyC):
    n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
               gameState[(x) % nxC, (y-1) % nyC] + \
               gameState[(x+1) % nxC, (y-1) % nyC] + \
               gameState[(x-1) % nxC, (y) % nyC] + \
               gameState[(x+1) % nxC, (y) % nyC] + \
               gameState[(x-1) % nxC, (y+1) % nyC] + \
               gameState[(x) % nxC, (y+1) % nyC] + \
               gameState[(x+1) % nxC, (y+1) % nyC]
    return n_neigh 

# Función para aplicar las reglas del juego de la vida
def Rules(gameState, newGameState, nxC, nyC):
    for y in range(0, nxC):
        for x in range(0, nyC):
            n_neigh = Neighbors(gameState, x, y, nxC, nyC)

            if gameState[x, y] == 1 and (n_neigh == 3 or n_neigh == 2):
                newGameState[x, y] = 1
            elif gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            elif gameState[x, y] == 1 and n_neigh > 3 or n_neigh < 2:
                newGameState[x, y] = 0


# Tamaño del tablero
nxC = int(input("Ingresa el número de filas: "))
nyC = int(input("Ingresa el número de columnas: "))

# Porcentaje de células vivas al inicio
seedPorcent = float(input("Ingrese el porcentaje de células vivas al inicio: "))

# Número de iteraciones
iteraciones = int(input("Ingrese el número de iteraciones: "))

# Set dimensión pygame
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

# Color de la terminal
bg = 25, 25, 25
screen.fill(bg)

# Dimensión de las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estados de las celdas (Vivas = 1; Muertas = 0;)
gameState = randomSeed(nxC, nyC, seedPorcent)

# Bucle de ejecución
while iteraciones > 0:
    
    # Copia
    newGameState = np.copy(gameState)
    
    screen.fill(bg) # Rellena pantalla
    time.sleep(0.1) # Tiempo antes de ejecutar

    for y in range(0, nxC):
        for x in range(0, nyC):
            Neighbors(gameState, x, y, nxC, nyC) # Llamamos a la función contar vecinos
            Rules(gameState, newGameState, nxC, nyC) # Llamamos a la funcion reglas
            #Poligono de cada celda
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1) # Dibuja la celda en 1
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0) # Dibuja la celda en 0

    gameState = np.copy(newGameState) # Actualizamos (refresh)
    pygame.display.flip() # print en pygame
    iteraciones -= 1 # contador para itineraciones

pygame.quit()
