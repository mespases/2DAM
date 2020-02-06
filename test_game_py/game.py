import pygame
import sys

ancho = 440
alto = 280
color_azul = (0,0,64)

class Bola(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargamos imagen de la bola
        self.image = pygame.image.load("C:\Users\miguel.espases\Pictures\pelota.png")
        self.rect = self.image.get_rect()
        # Posicion inicial de la pelota
        self.rect.centerx = ancho / 2
        self.rect.centery = alto / 2

        # Establecer velocidad inicial
        self.speed = [3,3]

    def update(self):
        # Evitar que la pelota salga de la pantalla
        if self.rect.bottom >= alto or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ancho or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        # Mover en base a la posicion actual
        self.rect.move_ip(self.speed)

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargamos imagen de la bola
        self.image = pygame.image.load("C:\Users\miguel.espases\Pictures\p.png")
        self.rect = self.image.get_rect()
        # Posicion inicial de la linea
        self.rect.midbottom = (ancho/2, alto-20)

        # Establecer velocidad inicial
        self.speed = [0,0]

    def update(self, evento):
        # Se mira haber si se ha presionado alguna flecha
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
            self.speed = [+5,0]
        else:
            self.speed = [0,0]

        # Mover en base a la posicion actual
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):

    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargamos imagen de la bola
        self.image = pygame.image.load("C:\Users\miguel.espases\Pictures\pelota.png")
        self.rect = self.image.get_rect()


        # Establecer velocidad inicial
        self.speed = [3,3]

# Pantalla del juego
pantalla = pygame.display.set_mode((ancho, alto))
# Nombre de la pantalla
pygame.display.set_caption("Juego de ladrillos")
# Crear reloj
reloj = pygame.time.Clock()
# Activar repeticion de evento de tecla presionada
pygame.key.set_repeat(10)

pelota = Bola()
jugador = Jugador()

while True:
    # Establecer FPS
    reloj.tick(60)

    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        # Buscar eventos del teclado
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)

    # Actualizar posicion de la pelota
    pelota.update()
    # Rellenar pantalla del color seleccionado
    pantalla.fill(color_azul)

    # Dibujar la pelota por pantalla
    pantalla.blit(pelota.image, pelota.rect)
    # Dibujar al jugador
    pantalla.blit(jugador.image, jugador.rect)
    pygame.display.flip()
