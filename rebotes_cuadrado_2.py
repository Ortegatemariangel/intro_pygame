import pygame
import sys
import random

rojo = (255, 0, 0)
amarillo = (255, 250, 0)
color3 = (0,250,255)
color4 = (50,120,125)
color5 = (57,255,20)
azul = (0, 0, 255)


ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("El cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

YY = 300

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO
    YY = YY + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3
    elif YY >= 450:
        YY = 450
        MOVIMIENTO = -3
    elif YY <= 0:
        YY = 0
        MOVIMIENTO = 3

    pygame.draw.rect(ventana, rojo, (XX, 0, 50, 50))
    pygame.draw.rect(ventana, amarillo, (0, YY, 50, 50))
    pygame.draw.rect(ventana, color3, (450, YY, 50, 50))
    pygame.draw.rect(ventana, color4, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, color5, (XX, YY, 20, 20))

    color_aleatorio = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    pygame.draw.rect(ventana, color_aleatorio, (200, 200, 100, 100))
    pygame.display.flip()