# importamos la librerìa pygame
import pygame
import random 

# inicializamos los mòdulos de pygame
pygame.init()

#  Establecer tìtulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Funciòn para generar un color aleatorio
def generar_color_aleatorio():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generamos un color aleatorio
color_aleatorio = generar_color_aleatorio()

# crear una superficie
superficie_aleatoria = pygame.Surface((300,300))

# Rellenamos la superficie de un color aleatorio
superficie_aleatoria.fill(color_aleatorio)

# Inserto o muevo la superficie de la ventana 
ventana.blit(superficie_aleatoria, (0,0))

# Actualiza la visualizaciòn de la ventana 
pygame.display.flip()