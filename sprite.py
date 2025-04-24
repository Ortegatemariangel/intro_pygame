import pygame
import random

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("juego de sprite")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect(center=(400, 550))

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += 5

# Clase Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect(center=(x, y))
        self.activa = True

    def update(self):
        if self.activa:
            self.rect.y -= 10
            if self.rect.bottom < 0:
                self.activa = False

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self.rect.y = -40
        self.activo = True

    def update(self):
        if self.activo:
            self.rect.y += 3
            if self.rect.top > 600:
                self.activo = False

# Crear los objetos
jugador = Jugador()
bala = None
enemigo = Enemigo()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and bala is None:
                bala = Bala(jugador.rect.centerx, jugador.rect.top)

    # Actualizar sprites individualmente
    jugador.update()
    if bala:
        bala.update()
        if not bala.activa:
            bala = None
    if enemigo:
        enemigo.update()
        if not enemigo.activo:
            enemigo = Enemigo()

    # Colisiones
    if bala and enemigo and bala.rect.colliderect(enemigo.rect):
        bala = None
        enemigo = Enemigo()

    # Dibujar todo
    pantalla.fill(NEGRO)
    pantalla.blit(jugador.image, jugador.rect)
    if bala:
        pantalla.blit(bala.image, bala.rect)
    if enemigo:
        pantalla.blit(enemigo.image, enemigo.rect)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()