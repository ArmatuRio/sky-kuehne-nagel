import random 

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

HEIGTH = 800
WIDTH = 1200
FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGTH))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGTH))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3


player_size = (20, 20)
player = pygame.image.load('player1.png').convert_alpha() #pygame.Surface(player_size)
# player.fill(COLOR_BLACK)
player_rect = player.get_rect()
player_move_down = [0, 4]
player_move_up = [0, -4]
player_move_right = [4, 0]
player_move_left = [-4, 0]

def create_enemy():
    enemy_size = (15, 15)
    enemy = pygame.image.load('enemy.png').convert_alpha() #pygame.Surface(enemy_size)
    # enemy.fill(COLOR_BLUE) # ONE
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGTH), *enemy_size)
    enemy_move = [random.randint(-8,-4), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (30, 30)
    bonus = pygame.image.load('bonus-kuehne-nagel.png').convert_alpha() #pygame.Surface(bonus_size)
    # bonus.fill(COLOR_GREEN) # ONE
    bonus_rect = pygame.Rect(random.randint(0, WIDTH),0, *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

GREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(GREATE_ENEMY, 1500)
GREATE_BONUS = pygame.USEREVENT + 2 # GREATE_ENEMY + 1
pygame.time.set_timer(GREATE_BONUS, 3000)

enemies = []
bonuses = []

score = 0

# playing = True   # ONE

# game_over = False
# victory = False


# game_over_message = FONT.render("Кінець Ігри", True, COLOR_RED)


# while playing:
#     FPS.tick(220)

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             playing = False
#         if event.type == GREATE_ENEMY:
#            enemies.append(create_enemy())
#         if event.type == GREATE_BONUS:
#             bonuses.append(create_bonus())

game_over_message = FONT.render("Кінець Ігри", True, COLOR_RED)
victory_message = FONT.render("Ви перемогли!", True, COLOR_GREEN)

game_over = False
victory = False

while not game_over and not victory:
    FPS.tick(220)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        if event.type == GREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == GREATE_BONUS:
            bonuses.append(create_bonus())


    # main_display.fill(COLOR_BLACK) # ONE
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < - bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < - bg.get_width():
        bg_X2 = bg.get_width()   

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGTH:
        player_rect = player_rect.move(player_move_down)
    
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)    


    # for enemy in enemies:            # ONE
    #  enemy[1] = enemy[1].move(enemy[2])
    #  main_display.blit(enemy[0], enemy[1])
    #  if player_rect.colliderect(enemy[1]):
    #     playing = False

    #  if bonus in bonuses:
    #      bonus[1] = bonus[1].move(bonus[2])
    #      main_display.blit(bonus[0], bonus[1])

    #  if player_rect.colliderect(bonus[1]):
    #      score += 1
    #      bonuses.pop(bonuses.index(bonus))

    #  if score >= 10:  # Замість 10 можна вибрати будь-яку іншу кількість очок
    #     playing = False

    # for enemy in enemies:  #TWO
    #     enemy[1] = enemy[1].move(enemy[2])
    #     main_display.blit(enemy[0], enemy[1])
    #     if player_rect.colliderect(enemy[1]):
    #         playing = False
    #         main_display.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width() // 2, HEIGTH // 2 - game_over_message.get_height() // 2))

    # for bonus in bonuses: #ONE
    #     bonus[1] = bonus[1].move(bonus[2])
    #     main_display.blit(bonus[0], bonus[1])

    #     if player_rect.colliderect(bonus[1]):
    #          score += 1
    #          bonuses.pop(bonuses.index(bonus))
    #          main_display.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width() // 2, HEIGTH // 2 - game_over_message.get_height() // 2))

    # main_display.blit(FONT.render(str(score),True, COLOR_BLACK), (WIDTH-50, 20))
    # main_display.blit(player, player_rect)

    # pygame.display.flip()

    # for enemy in enemies:
    #     if enemy[1].left < 0:
    #         enemies.pop(enemies.index(enemy))
    # for bonus in bonuses:
    #     if bonus[1].top > HEIGTH:
    #         bonuses.pop(bonuses.index(bonus))        

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            game_over = True
            main_display.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width() // 2, HEIGTH // 2 - game_over_message.get_height() // 2))

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
             score += 1
             bonuses.pop(bonuses.index(bonus))

    if score >= 10:
        victory = True
        main_display.blit(victory_message, (WIDTH // 2 - victory_message.get_width() // 2, HEIGTH // 2 - victory_message.get_height() // 2))

    main_display.blit(FONT.render(str(score),True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    if game_over or victory:
        pygame.display.flip()
        FPS.tick(1)  # Змініть це значення за потреби
        continue

    pygame.display.flip()
    FPS.tick(220)