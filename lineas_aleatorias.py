import pygame
import sys
import random


verde = (255, 143, 0)
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul = (0,0,255)
rojo = (255,0,0)
rosado = (255,192,203)

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Lineas aleatorias")

fuente_arial = pygame.font.SysFont("arial", 30, 1, 1)

clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(rosado)  

    texto = fuente_arial.render("Colegio San José De Guanentá", True, azul)
    ventana.blit(texto, (25, 25))

    sistemas = fuente_arial.render("Especialidad de sistemas", True, azul)
    ventana.blit(sistemas, (70, 60))

    nombre = fuente_arial.render("Mariangel Ortegate", True, azul)
    ventana.blit(nombre, (0, 470))

    pygame.draw.rect(ventana, verde, (50, 110,375,320 ),2)

    for i in range(100):
        x1 = random.randint(50, 420)
        y1 = random.randint(110,420)
        x2 = random.randint(50, 420)
        y2 = random.randint(110,420)

        color_aleatorio = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pygame.draw.line(ventana, color_aleatorio, (x1, y1), (x2,y2))

        

    pygame.display.flip()
