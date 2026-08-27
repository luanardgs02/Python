import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo de Carro Desviando de Obstáculos')

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Configurações do carro
car_width = 50
car_height = 100
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 20
car_speed = 5

# Configurações dos obstáculos
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 5
obstacles = []

# Pontuação
score = 0
font = pygame.font.Font(None, 36)

def draw_car(x, y):
    pygame.draw.rect(screen, red, (x, y, car_width, car_height))

def create_obstacle():
    x = random.randint(0, screen_width - obstacle_width)
    y = -obstacle_height
    obstacles.append([x, y])

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, black, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

def update_obstacles():
    global score
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            score += 1

def collision_check(car_x, car_y, obstacles):
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if car_rect.colliderect(obstacle_rect):
            return True
    return False

def display_score():
    score_text = font.render("Pontuação: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

def game_over_screen():
    screen.fill(white)

    # Exibe a pontuação final
    game_over_text = font.render("Fim de Jogo! Pontuação: " + str(score), True, black)
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 100))

    # Botão "Reiniciar"
    restart_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
    pygame.draw.rect(screen, green, restart_button)
    restart_text = font.render("Reiniciar", True, white)
    screen.blit(restart_text, (screen_width // 2 - 50, screen_height // 2 + 10))

    # Botão "Sair"
    quit_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 80, 200, 50)
    pygame.draw.rect(screen, red, quit_button)
    quit_text = font.render("Sair", True, white)
    screen.blit(quit_text, (screen_width // 2 - 30, screen_height // 2 + 90))

    pygame.display.flip()

    # Aguarda a interação do jogador
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    return True  # Reiniciar o jogo
                if quit_button.collidepoint(mouse_pos):
                    return False  # Sair do jogo

# Loop do jogo
def main():
    global car_x, car_y, obstacles, score
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed

        if random.randint(0, 100) < 5:  # Probabilidade de criar um novo obstáculo
            create_obstacle()

        update_obstacles()

        if collision_check(car_x, car_y, obstacles):
            print("Fim de Jogo! Pontuação:", score)
            if game_over_screen():
                # Reinicia o jogo
                car_x = screen_width // 2 - car_width // 2
                car_y = screen_height - car_height - 20
                obstacles = []
                score = 0
            else:
                running = False

        screen.fill(white)
        draw_car(car_x, car_y)
        draw_obstacles()
        display_score()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()