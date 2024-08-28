import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('snail game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
game_active = False

start_time = 0

sky_surface = pygame.image.load('sky - Copy.png').convert()
ground_surface = pygame.image.load('ground.png').convert()

# score_surface = test_font.render('My game ', False, (65,64,40))
# score_rect = score_surface.get_rect(center = (400,50))


snail_surf = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0
#intro screen
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('press space to start',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,300))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                     player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and  player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#71BCE1', score_rect)
        # pygame.draw.rect(screen,'#71BCE1',score_rect,10)
        #
        # screen.blit(score_surface,score_rect)

        display_score()

        snail_rect.x -= 10
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)
        screen.blit(player_surf,player_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)



    # collision
        if snail_rect.colliderect(player_rect):
             game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)

    pygame.display.update()
    clock.tick(60)  # speed of snail
