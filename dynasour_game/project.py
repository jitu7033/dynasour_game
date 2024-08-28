import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks()) - start_time
    score_surf = test_font.render(f'score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)

                screen.blit(snail_surf, obstacle_rect)
                obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

            else:
                screen.blit(fly_surf,obstacle_rect)
                screen.blit(fly_surf,obstacle_rect)
                obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list

    else: return []

def collision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True

def player_animation():
    global player_surf,player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

    # player working animation if the player is on floor


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('snail game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
game_active = False

start_time = 0
score = 0
bg_music = pygame.mixer.Sound('music (1).wav')
bg_music.play(loops = -1)

jump_sound = pygame.mixer.Sound('audio_jump.mp3')



sky_surface = pygame.image.load('sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()

# snail_obasticle
snail_frame1 = pygame.image.load('snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('snail2.png').convert_alpha()
snail_frame_index = 0
snail_frames = [snail_frame1,snail_frame2]
snail_surf = snail_frames[snail_frame_index]

# fly_surface
fly_frame1 = pygame.image.load('Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('Fly2.png').convert_alpha()
fly_frame_index = 0
fly_frames = [fly_frame1,fly_frame2]
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk1 = pygame.image.load('player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('jump.png').convert_alpha()
player_surf = player_walk[player_index]
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

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)


fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)


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
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks())


        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        score = display_score()

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)


        # obsticle movment
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        # collision
        game_active = collision(player_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        score_message = test_font.render(f'your score : {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)# speed of snail


