import pygame
import random
import time

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pegue o Quadrado")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)

# Fonte para exibir texto
fonte = pygame.font.SysFont(None, 55)

# Posição inicial do jogador e do alvo
jogador = pygame.Rect(350, 250, 50, 50)
alvo = pygame.Rect(random.randint(0, largura-50), random.randint(0, altura-50), 50, 50)

# Velocidade do jogador
velocidade = 3  # Reduzida para 3

# Pontuação e tempo
pontuacao = 0
tempo_inicial = time.time()  # Tempo inicial do jogo

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # Impede que o jogador saia da tela
    if jogador.left < 0:
        jogador.left = 0
    if jogador.right > largura:
        jogador.right = largura
    if jogador.top < 0:
        jogador.top = 0
    if jogador.bottom > altura:
        jogador.bottom = altura

    # Verifica colisão entre jogador e alvo
    if jogador.colliderect(alvo):
        alvo.x = random.randint(0, largura-50)
        alvo.y = random.randint(0, altura-50)
        pontuacao += 1  # Incrementa a pontuação

    # Calcula o tempo decorrido
    tempo_decorrido = int(time.time() - tempo_inicial)

    # Desenha na tela
    tela.fill(branco)
    pygame.draw.rect(tela, azul, jogador)
    pygame.draw.rect(tela, vermelho, alvo)

    # Exibe a pontuação e o tempo na tela
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, preto)
    texto_tempo = fonte.render(f"Tempo: {tempo_decorrido}", True, preto)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_tempo, (10, 60))

    pygame.display.flip()

# Finaliza o pygame
pygame.quit()