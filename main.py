import pygame

# constante et variables
white = (255, 255, 255)
black = (0, 0, 0)

width = 600
height = 600

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

delay = 30

raquette_vitesse = 20

raquette_taille = 10
raquette_hauteur = 100

j1_x_pos = 10
j1_y_pos = height / 2 - raquette_hauteur / 2

j2_x_pos = width - raquette_taille - 10
j2_y_pos = height / 2 - raquette_hauteur / 2

j1_score = 0
j2_score = 0

j1_haut = False
j1_bas = False
j2_haut = False
j2_bas = False

ball_x_pos = width / 2
ball_y_pos = height / 2
ball_width = 8
ball_x_vel = -10
ball_y_vel = 0

screen = pygame.display.set_mode((width, height))


# Objets
def draw_objects():
    pygame.draw.rect(screen, white, (int(j1_x_pos), int(j1_y_pos), raquette_taille, raquette_hauteur))
    pygame.draw.rect(screen, white, (int(j2_x_pos), int(j2_y_pos), raquette_taille, raquette_hauteur))
    pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(j1_score)} - {str(j2_score)}", False, white)
    screen.blit(score, (width / 2, 30))


def mouvement_joueur():
    global j1_y_pos
    global j2_y_pos

    if j1_haut:
        j1_y_pos = max(j1_y_pos - raquette_vitesse, 0)
    elif j1_bas:
        j1_y_pos = min(j1_y_pos + raquette_vitesse, height)
    if j2_haut:
        j2_y_pos = max(j2_y_pos - raquette_vitesse, 0)
    elif j2_bas:
        j2_y_pos = min(j2_y_pos + raquette_vitesse, height)


def mouvement_ball():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global j1_score
    global j2_score

    if (ball_x_pos + ball_x_vel < j1_x_pos + raquette_taille) and (
            j1_y_pos < ball_y_pos + ball_y_vel + ball_width < j1_y_pos + raquette_hauteur):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (j1_y_pos + raquette_hauteur / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel < 0:
        j2_score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_vel = 10
        ball_y_vel = 0
    if (ball_x_pos + ball_x_vel > j2_x_pos - raquette_taille) and (
            j2_y_pos < ball_y_pos + ball_y_vel + ball_width < j2_y_pos + raquette_hauteur):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (j2_y_pos + raquette_hauteur / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel > height:
        j1_score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_vel = -10
        ball_y_vel = 0
    if ball_y_pos + ball_y_vel > height or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel


pygame.display.set_caption("Alfheim-Pong de l'UCLouvain")
screen.fill(black)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_z:
                j1_haut = True
            if event.key == pygame.K_s:
                j1_bas = True
            if event.key == pygame.K_UP:
                j2_haut = True
            if event.key == pygame.K_DOWN:
                j2_bas = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = True
            if event.key == pygame.K_z:
                j1_haut = False
            if event.key == pygame.K_s:
                j1_bas = False
            if event.key == pygame.K_UP:
                j2_haut = False
            if event.key == pygame.K_DOWN:
                j2_bas = False

    screen.fill(black)
    mouvement_joueur()
    mouvement_ball()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(delay)
