import pygame
import time
import random

pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamaño de pantalla
ancho = 600
alto = 400

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente - Proyecto Integrador')

reloj = pygame.time.Clock()
tamaño_celda = 20
velocidad = 10
fuente = pygame.font.SysFont("comicsansms", 25)

def mostrar_puntaje(score):
    valor = fuente.render("Puntaje: " + str(score), True, rojo)
    pantalla.blit(valor, [0, 0])

def juego():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2
    x1_cambio = 0
    y1_cambio = 0
    serpiente = []
    largo_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_celda) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamaño_celda) / 20.0) * 20.0

    while not game_over:
        while game_close:
            pantalla.fill(azul)
            mensaje = fuente.render("Perdiste! Presiona C para continuar o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntaje(largo_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_celda
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_celda
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_celda, tamaño_celda])
        cabeza_serpiente = [x1, y1]
        serpiente.append(cabeza_serpiente)
        if len(serpiente) > largo_serpiente:
            del serpiente[0]

        for segment in serpiente[:-1]:
            if segment == cabeza_serpiente:
                game_close = True

        for segment in serpiente:
            pygame.draw.rect(pantalla, blanco, [segment[0], segment[1], tamaño_celda, tamaño_celda])

        mostrar_puntaje(largo_serpiente - 1)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_celda) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamaño_celda) / 20.0) * 20.0
            largo_serpiente += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

juego()
