import pygame
import sys

# inicializar los modlos
pygame.init()
pygame.mixer.init()

#colores

COLOR_BLANCO = pygame.Color(255,255,255)

#ventana
PANTALLA = pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("Soidos en Pygame")

continuar = True

#Sonido de fondo
SILBATO = pygame.mixer.music.load("sounds/silbato.ogg")
pygame.mixer.music.play(1,0.0)

# efectos sonoros 
GALLO = pygame.mixer.Sound("sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("sounds/cuervo.ogg")
BICI = pygame.mixer.Sound("sounds/timbre.ogg")

#bucle del juego

while continuar:
    for event in pygame.event.get():
        # Cierra la ventana si se hace click en el boton de cerrar ventana
        if event.type == pygame.QUIT:
            continuar = False
        # detecta si se opriio una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuar == False
            elif event.key == pygame.K_o:
                GALLO.play()
            elif event.key == pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_v:
                BICI.play()
            elif event.key == pygame.K_DOWN:
                VOLUMEN = pygame.mixer.music.get_volume() - 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)
            elif event.key == pygame.K_UP:
                VOLUMEN = pygame.mixer.music.get_volume() + 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)

pygame.display.flip()
        