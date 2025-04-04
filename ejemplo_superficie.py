# Importamos la libreria pygame
import pygame
import random

# Inicializamos los modulos de pygame
pygame.init()

# Establecer titulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensones de la ventana
ventana = pygame.display.set_mode((400,400))

# definir un color
azul = random.randint(0,256)
amarillo = random.randint(0,256)
rojo = random.randint(0,256)
color_aleatorio=((azul,amarillo,rojo))

# Crear una superficie

color_aleatorio_aleatoria = pygame.Surface((200,200))

# Rellenamos la superficie
color_aleatorio.fill(azul, amarillo, rojo)

# Inserto la superficie de la ventana
ventana.blit(color_aleatorio, (100,100))

# Actualiza la visualizacion de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()