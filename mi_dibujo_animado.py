import pygame
import sys

verde = (255, 143, 0)
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul = (0,0,255)
rojo = (255,0,0)
rosado = (255,192,203)
cian = (0,255,255)
naranja = (255,165,0)
amarillo = (255,255,0)

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dibujito animado")

fuente_arial = pygame.font.SysFont("arial", 30, 1, 1)

clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(negro)  

    texto = fuente_arial.render("Colegio San José De Guanentá", True, amarillo)
    ventana.blit(texto, (25, 25))

    sistemas = fuente_arial.render("Especialidad de sistemas", True, amarillo)
    ventana.blit(sistemas, (70, 60))

    nombre = fuente_arial.render("Mariangel Ortegate", True, amarillo)
    ventana.blit(nombre, (0, 470))

    # cielo y pasto
    ventana.fill(cian) 
    pygame.draw.rect(ventana, verde, (0, 350, 500, 150))

    # Nubes
    pygame.draw.circle(ventana, blanco, (100, 100), 25)
    pygame.draw.circle(ventana, blanco, (120, 90), 30)
    pygame.draw.circle(ventana, blanco, (140, 100), 25)

    pygame.draw.circle(ventana, blanco, (300, 80), 20)
    pygame.draw.circle(ventana, blanco, (320, 70), 25)
    pygame.draw.circle(ventana, blanco, (340, 80), 20)

    
    # Tronco del tren 
    pygame.draw.rect(ventana, rosado, (140,280,280,140) )
    
    # Union de las llantas
    pygame.draw.rect(ventana, negro, (160,415,395,40) )

    # cabina
    pygame.draw.rect(ventana, rosado, (210,90,200,220) )
    # Ventana de la cabina
    pygame.draw.rect(ventana, blanco, (230,105,155,190) )
    # Circulo y rectangulo delantero del tren
    pygame.draw.circle(ventana, rosado, (120,350), 55)
    pygame.draw.rect(ventana, rosado, (90,250,30,200) )

    # Rectangulo de arriba de la ventana
    pygame.draw.rect(ventana, rosado, (180,100,250,100) )
    # Chimenea
    pygame.draw.rect(ventana, rosado, (145,230,30,190) )
    # Llantas
    # Llanta de el centro
    pygame.draw.circle(ventana, blanco, (280,430), 40)
    # Llanta derecha
    pygame.draw.circle(ventana, blanco, (375,430), 40)
    # Llanta izquierda
    pygame.draw.circle(ventana, blanco, (190,430), 40)
    # Carita
    pygame.draw.circle(ventana, naranja, (310,250), 45)
    # ojos
    pygame.draw.circle(ventana, blanco, (330,235), 10)
    pygame.draw.circle(ventana, blanco, (290,235), 10)
    # Pupila
    pygame.draw.circle(ventana, azul, (330,235), 5)
    pygame.draw.circle(ventana, azul, (290,235), 5)
    # Boca
    pygame.draw.circle(ventana, negro, (310,270), 10)
    
    pygame.display.flip()
    