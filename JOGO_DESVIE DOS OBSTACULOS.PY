import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Evite os Obstáculos")

# Cores
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Fonte
fonte = pygame.font.Font(None, 36)

# Jogador
jogador = pygame.Rect(375, 500, 50, 50)

# Obstáculos
obstaculos = []
velocidade = 5

# Pontuação
pontuacao = 0

# Função para explodir obstáculos próximos
def explodir_obstaculos(jogador, obstaculos):
    area_explosao = pygame.Rect(jogador.x - 50, jogador.y - 50, 150, 150)  # Área de explosão
    obstaculos[:] = [obs for obs in obstaculos if not area_explosao.colliderect(obs)]  # Remove obstáculos na área

# Função para exibir a tela de "Fim de Jogo"
def tela_fim_de_jogo(pontuacao):
    tela.fill(PRETO)

    # Exibe a pontuação final
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontuacao, (LARGURA // 2 - 100, ALTURA // 2 - 100))

    # Botão "Reiniciar"
    botao_reiniciar = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2, 200, 50)
    pygame.draw.rect(tela, VERDE, botao_reiniciar)
    texto_reiniciar = fonte.render("Reiniciar", True, BRANCO)
    tela.blit(texto_reiniciar, (LARGURA // 2 - 50, ALTURA // 2 + 10))

    # Botão "Sair"
    botao_sair = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 + 80, 200, 50)
    pygame.draw.rect(tela, VERMELHO, botao_sair)
    texto_sair = fonte.render("Sair", True, BRANCO)
    tela.blit(texto_sair, (LARGURA // 2 - 30, ALTURA // 2 + 90))

    pygame.display.flip()

    # Aguarda a interação do jogador
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False  # Sair do jogo
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_reiniciar.collidepoint(mouse_pos):
                    return True  # Reiniciar o jogo
                if botao_sair.collidepoint(mouse_pos):
                    return False  # Sair do jogo

# Loop principal
def main():
    global pontuacao, obstaculos, jogador

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador.x > 0:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT] and jogador.x < LARGURA - 50:
            jogador.x += velocidade

        # Adiciona novos obstáculos
        if random.randint(0, 100) < 5:
            obstaculos.append(pygame.Rect(random.randint(0, LARGURA - 50), 0, 50, 50))

        # Movimenta os obstáculos e verifica colisão
        for obstaculo in obstaculos:
            obstaculo.y += velocidade
            if obstaculo.colliderect(jogador):  # Verifica colisão com o jogador
                if tela_fim_de_jogo(pontuacao):  # Exibe a tela de "Fim de Jogo"
                    # Reinicia o jogo
                    pontuacao = 0
                    obstaculos = []
                    jogador.x = 375
                else:
                    executando = False  # Sai do jogo
            if obstaculo.y > ALTURA:  # Remove obstáculos que saíram da tela
                obstaculos.remove(obstaculo)
                pontuacao += 1  # Incrementa a pontuação

        # Explode obstáculos ao pressionar "Space"
        if teclas[pygame.K_SPACE]:
            explodir_obstaculos(jogador, obstaculos)

        # Desenha na tela
        tela.fill(PRETO)
        pygame.draw.rect(tela, AZUL, jogador)  # Desenha o jogador
        for obstaculo in obstaculos:
            pygame.draw.rect(tela, VERMELHO, obstaculo)  # Desenha os obstáculos

        # Exibe a pontuação
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontuacao, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()