# Estructura de un juego en pygame

## Inicializaciòn

- Como todo programa en pytho se deben importar los modulos o librerias a utilizar
`import pygame`

- Inicializar pygame usuando la funcion init (). Inicializa todos los mòdulos de pygame importados.
`pygame.init()`

## Visualizaciòn de la ventana

`ventana = pygame.display.set_mode((600, 400))`

- set_mode() es la funcion encargada de definir el tamaño de la ventana. En el ejemplo, se esta definiendo una ventana de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("Mi ventana")`

- set_caption() es la funcion que añade un titulo a la ventana.

### Funcion set_mode()
`set_mode(size =(0,0) flags = 0, depht = 0, display = 0)`
- size = (600,400) : define el tamaño de la ventana.

- flags : define uno omas comportamientos para la ventana.
    - valores :
        - pygame.FULLSCREEN
        - pygame.SESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame,
        RESIZABLE: pantalla completa.
        dimensiones modificables.

## Bucle del juego - game loop
- Bucle infinito que se interrumpira al cumplir ciertos criterios.
- Reloj iterno del juego.
- En cada iteracion del bucle del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado a otro, o que se ha cruzado la linea de llegada lo que quiere decir ue la partida ha terminado.
- Cada iteracion es un oportunidad para actualizar todos los datos relacionados con el estado actual de la partida.
- En cada iteracion se realizan las siguientes tareas:
    1. Comprobar que no se alcanzan las condiciones de parada en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteracion actual.
    3. Obtener las entradas del sistema, o de interaccion con el jugador.
    4. Actualizar todas las entidades que caracterizan el juego.
    5. Refrescar la pantalla.

    ## Superficies pygame
    - SUperficie: 
       - Elemento geometrico.
       - Linea, poligono, imagen, texto que se muestra en la pantalla
       - El poligono se puede o no rellenar de color.
       - Las superficies se crean de diferente manera dependiendo del tipo: 
            - imagen: image.load()
            - texto: font.render()
            - Superficie generica: pygame.Superface()
            - Ventana del juego: pygame.display.set_mode()

# Ejemplo bandera de Colombia

```Python

# Establecer tìtulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Colores de la bandera
amarillo = (255, 255, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)


# crear una superficie
superficie_amarillo = pygame.Surface((400,200))
superficie_azul = pygame.Surface((400, 100))
superficie_rojo = pygame.Surface((400, 100))

# Rellenamos la superficie de color amarillo, azul, rojo
superficie_amarillo.fill(amarillo)
superficie_azul.fill(azul)
superficie_rojo.fill(rojo)

# Inserto o muevo la superficie de la ventana 
ventana.blit(superficie_amarillo, (0,0))
ventana.blit(superficie_azul, (0,200))
ventana.blit(superficie_rojo, (0,300))

# Actualiza la visualizacion de la ventana 
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

```
### Resultado

![screen](screen.jpg)

## Gestion del tiempo y los eventos.

### Modulo time

- Ofrece varias funciones que permite cronometrar la sesion actual desde el (init) o pausar, la ejecucion, por ejemplo.
- Funciones. 
    - pygame.time.get_ticks
    - pygame.time.waitpygame.time.delay

- Objeto clock
    - La funcion tick permite actualizar el reloj asociado con el juego actual.
    - Se llama cada vez que se actualiza la pantalla del juego.
    - Permite especificar el numero maximo de fotogramas que se muestran por segundo, y por tanto, limitar y controlar la velocidad de ejecucion del juego.
    - Si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca se ira mas rapido de 50 fotogramas por segundo: `Clock.tick(50)`

### Gestion de eventos.

- Hay diferentes formas para que el programa sepa que se ha desencadenado un evento.
- Es esencial que los programas puedan conocer inmediatamente las acciones del jugador atraves del telado, el mouse, el joystick o cualquier otro periferico.

#### Funcion pygame.event.get
- Permite obtener todos los eventos en espera de ser procesados y que estan disponibles en una cola. 
- Si no hay ninhuno, se obtiene una coleccion vacia.

```python
# Usamos un bucle for para recorrer todos los eventos de la coleccion obtenida al llamar a la funcion get.
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SCAPE:
            PARAR_JUEGO = True
```

#### Funcion pygame.event.wait
- Esta funcion espera a que ocurra un evento, y en cuanto sucede esta disponible.

```python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```

#### Funcion pygame.event.poll
- Devuelve solo uno de los eventos que esta en la cola de espera.


## Sonidos en pygame
- pygame.mixer : Modulo que permite la gestion del sonido.
- music : submodulo que gestiona la musica de fondo. Necesariamente solo hay una a la vez.
- Sound : Objeto de mixer, que se puede instanciar varias veces para usarlo en los efectos del sonido del juego.

### Archivos de sonidos
- Se recomienda usar dos formatos, principalmente:
    - Formato WAV (Waveform Audio File Format)
    - Formato abierto y gratuito OGG

### Channel (Canal) en pygame
- Un juego tiene varios canales de sonido.
- Se puede asignar un sonido al canal numero 1 y otro diferente al numero 2.
- Entonces es posible reproducir sonidos simultaneamente activando su lectura en diferente canales.

## Sprites
- Objeto que asocia una ubicacion, una representacion grafica (esta o aquella imagen, por ejemplo) y un conjunto de propiedades.

- Estas propiedades pueden ser un nombre, un texto, valores buleanos que caracterizan el objeto en cuestión (por ejemplo si el objeto se puede mover o no)

- Una posible traduccion del termino sprite podria ser "imagen-objeto" que se actualiza con cada actualizacion del bucle del juego

- Cuanto más complejo es el juego más objetos grafico tiene que gestionar y actualizar lo que puede ser tedioso

- Pygame usa no solo la nocion de sprites sino tambien de grupos de sprites(group)

- La nocion de group permite agrupar los objetos del mismo tipo. Ejemplo: todos los soldados de un ejercito lo que se entiende como una coleccion de instancias de una clase Soldado.

- Un determinado procesamiento se puede aplicara un conjunto o subconjunto de sprites. Ejemplo: cambiar el color de todos los enemigos o hacer invisibles algunos objetos 

## ¿Qué es un Sprite?
- Un Sprite es una representación gráfica de un objeto dentro de un juego. Puede moverse, detectar colisiones y agruparse con otros sprites para un mejor manejo.
   - ```pygame.sprite.Sprite``` es una clase base en pygame que facilita estas funcionalidades.

### ¿Para qué se usa un sprite?

- Mostrar personajes u objetos en pantalla
Ej: el jugador, enemigos, balas, monedas, obstáculos, etc.

- Controlar posición y movimiento

- Un sprite tiene un atributo .rect que define dónde está en la pantalla y qué espacio ocupa. Puedes moverlo cambiando .rect.x o .rect.y.

- Detectar colisiones

- Pygame tiene funciones como pygame.sprite.collide_rect() o pygame.sprite.groupcollide() que permiten detectar si dos sprites se están tocando.

- Actualizar su estado

- Puedes crear un método .update() que cambia su comportamiento en cada frame (por ejemplo, moverse, animarse, seguir al jugador, etc.).

- Organizar lógicamente los elementos del juego

- Se pueden agrupar sprites en Groups para manejar muchos objetos a la vez (actualizarlos, dibujarlos, detectar colisiones en lote, etc.).

### Ejemplo de juego
- Importamos la libreria necesaria
import pygame
import random
- Inicializamos la ventana y le ponemos nombre y tamaño

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("juego de sprite")
reloj = pygame.time.Clock()

- Definimos colores

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

- Definimos el jugador

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
- Explicacion

- class Jugador(pygame.sprite.Sprite):

     - Aquí definimos una clase llamada Jugador, que hereda de pygame.sprite.Sprite. Esto significa que Jugador es un tipo de sprite en Pygame y tiene todas las capacidades de un sprite, como la posición (rect), el dibujo en pantalla (image), etc.

- def __init__(self):

     - El constructor de la clase Jugador, se llama cuando creas una nueva instancia de Jugador.

- self.image = pygame.Surface((50, 50))

     - Creamos una superficie cuadrada de 50x50 píxeles para representar al jugador.

- self.image.fill(AZUL)

     - Llenamos la superficie con el color azul.

- self.rect = self.image.get_rect(center=(400, 550))

     - Obtenemos el rectángulo (rect) de la superficie del jugador, y lo colocamos en el centro de las coordenadas (400, 550).

- def update(self):

     - Este método se llama en cada iteración del bucle del juego. Se usa para actualizar la lógica del jugador, como el movimiento.

- teclas = pygame.key.get_pressed()

     - Obtiene el estado de todas las teclas (si están presionadas o no).

- if teclas[pygame.K_LEFT] and self.rect.left > 0:

     - Si la tecla de flecha izquierda está presionada y el jugador no está fuera del borde izquierdo, mueve al jugador 5 píxeles hacia la izquierda.

- if teclas[pygame.K_RIGHT] and self.rect.right < 800:

     - Similar, pero para mover el jugador a la derecha si la tecla de flecha derecha está presionada y no sale del borde derecho de la pantalla (800 píxeles).



## Sprite group

- El uso de ```pygame.sprite.Group``` es una de las características más poderosas de Pygame para trabajar con múltiples sprites al mismo tiempo. Te permite organizar, actualizar y dibujar muchos sprites de forma eficiente y sencilla.

### Usos de sprite group

- Actualizar todos los sprites a la vez con .update()

- Dibujar todos los sprites en pantalla con .draw(superficie)

- Detectar colisiones entre grupos o dentro de ellos

## Ejemplo de juego

- Para este juego usamos el mismo codigo con la diferencia que se añade sprite groups lo cual permite que hayan varios enemigos al mismo tiempo

- Se usan para organizar y manejar múltiples sprites fácilmente. Group permite actualizar y dibujar todos los sprites a la vez.

todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()