import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Raquetes e bola
raquete1 = pygame.Rect(50, 250, 10, 100)
raquete2 = pygame.Rect(740, 250, 10, 100)
bola = pygame.Rect(395, 295, 10, 10)

# Velocidades
velocidade_raquete = 5
velocidade_bola_x = 3 * random.choice((1, -1))
velocidade_bola_y = 3 * random.choice((1, -1))

# Pontuação
pontuacao1 = 0
pontuacao2 = 0
fonte = pygame.font.Font(None, 74)

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Movimentação das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1.top > 0:
        raquete1.y -= velocidade_raquete
    if teclas[pygame.K_s] and raquete1.bottom < altura:
        raquete1.y += velocidade_raquete
    if teclas[pygame.K_UP] and raquete2.top > 0:
        raquete2.y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and raquete2.bottom < altura:
        raquete2.y += velocidade_raquete

    # Movimentação da bola
    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y

    # Colisão da bola com as raquetes
    if bola.colliderect(raquete1) or bola.colliderect(raquete2):
        velocidade_bola_x *= -1

    # Colisão da bola com as bordas superior e inferior
    if bola.top <= 0 or bola.bottom >= altura:
        velocidade_bola_y *= -1

    # Pontuação
    if bola.left <= 0:
        pontuacao2 += 1
        bola.center = (largura // 2, altura // 2)
        velocidade_bola_x *= random.choice((1, -1))
        velocidade_bola_y *= random.choice((1, -1))
    if bola.right >= largura:
        pontuacao1 += 1
        bola.center = (largura // 2, altura // 2)
        velocidade_bola_x *= random.choice((1, -1))
        velocidade_bola_y *= random.choice((1, -1))

    # Desenha na tela
    tela.fill(preto)
    pygame.draw.rect(tela, branco, raquete1)
    pygame.draw.rect(tela, branco, raquete2)
    pygame.draw.ellipse(tela, branco, bola)

    # Exibe a pontuação
    texto1 = fonte.render(str(pontuacao1), True, branco)
    texto2 = fonte.render(str(pontuacao2), True, branco)
    tela.blit(texto1, (largura // 4, 10))
    tela.blit(texto2, (3 * largura // 4, 10))

    pygame.display.flip()

    # Controla a taxa de atualização
    pygame.time.Clock().tick(60)

# Finaliza o pygame
pygame.quit()