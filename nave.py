import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🚀 Juego de Nave")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Jugador (nave)
nave = pygame.Rect(375, 500, 50, 50)
vel_nave = 5

# Balas
balas = []
vel_bala = 7

# Enemigos
enemigos = []
vel_enemigo = 2

def crear_enemigos():
    for _ in range(5):
        x = random.randint(0, ANCHO - 50)
        y = random.randint(-100, -40)
        enemigos.append(pygame.Rect(x, y, 50, 50))

crear_enemigos()

# Bucle del juego
reloj = pygame.time.Clock()
jugando = True

while jugando:
    reloj.tick(60)
    pantalla.fill(NEGRO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                bala = pygame.Rect(nave.centerx - 2, nave.top, 5, 10)
                balas.append(bala)

    # Movimiento de la nave
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and nave.left > 0:
        nave.x -= vel_nave
    if teclas[pygame.K_RIGHT] and nave.right < ANCHO:
        nave.x += vel_nave

    # Movimiento de balas
    for bala in balas[:]:
        bala.y -= vel_bala
        if bala.bottom < 0:
            balas.remove(bala)

    # Movimiento de enemigos
    for enemigo in enemigos[:]:
        enemigo.y += vel_enemigo
        if enemigo.top > ALTO:
            enemigos.remove(enemigo)
            enemigos.append(pygame.Rect(random.randint(0, ANCHO - 50), random.randint(-100, -40), 50, 50))

    # Colisiones
    for enemigo in enemigos[:]:
        for bala in balas[:]:
            if enemigo.colliderect(bala):
                enemigos.remove(enemigo)
                balas.remove(bala)
                enemigos.append(pygame.Rect(random.randint(0, ANCHO - 50), random.randint(-100, -40), 50, 50))
                break

    # Dibujar
    pygame.draw.rect(pantalla, BLANCO, nave)
    for bala in balas:
        pygame.draw.rect(pantalla, BLANCO, bala)
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()

pygame.quit()
sys.exit()

