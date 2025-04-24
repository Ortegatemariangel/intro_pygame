import pygame
import random

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo con Sprite")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Clase del Jugador
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

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.add(bala)
        todos_los_sprites.add(bala)

# Clase de Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

# Clase de Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 3
        if self.rect.top > 600:
            self.kill()

# Grupos
todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()

# Crear jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Generar enemigos periódicamente
ENEMIGO_EVENTO = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMIGO_EVENTO, 1000)  # Cada 1000 ms

# Bucle del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.disparar()
        elif evento.type == ENEMIGO_EVENTO:
            enemigo = Enemigo()
            enemigos.add(enemigo)
            todos_los_sprites.add(enemigo)

    # Lógica del juego
    todos_los_sprites.update()

    # Verificar colisiones: balas vs enemigos
    colisiones = pygame.sprite.groupcollide(enemigos, balas, True, True)

    # Dibujar
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

    # Control de FPS
    reloj.tick(60)

pygame.quit()