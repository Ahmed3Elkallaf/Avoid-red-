import pygame
import random
pygame.font.init()


screen = pygame.display.set_mode((800,600))
FONT = pygame.font.SysFont("comicsans",30)


run = True

player_scale_x = 60
player_scale_y = 60

rx = random.randint(0,750)
rx2 = random.randint(0,750)
rx3 = random.randint(0,750)

ground = pygame.Rect((0,520,800,80))
player = pygame.Rect((20,460,player_scale_x,player_scale_y))
red = pygame.Rect((rx,0,20,50))
red2 = pygame.Rect((rx2,0,20,50))
red3 = pygame.Rect((rx3,0,20,50))
red4 = pygame.Rect((-40,480,40,40))


Jump = False
lose = False
vel_x = 10
vel_y = 15
red_speed = 4
active_red4 = 0
score = 0


def draw_red():
    pygame.draw.rect(screen,("red"),red)
    pygame.draw.rect(screen,("red"),red2)
    pygame.draw.rect(screen,("red"),red3)
    pygame.draw.rect(screen,("red"),red4)


clock = pygame.time.Clock()

while run:
    clock.tick(60)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,("blue"),player)
    pygame.draw.rect(screen,("white"),ground)
    draw_red()

    if not lose:
        red.y += red_speed
        red2.y += red_speed + 0.3
        red3.y += red_speed + 0.5

    if red.colliderect(ground) and not lose:
        rx = random.randint(0,800)
        red.x = rx
        red.y = 0
        red_speed += 0.2
        active_red4 += 1
        score += 1

    if red2.colliderect(ground) and not lose:
        rx2 = random.randint(0,800)
        red2.x = rx2
        red2.y = 0
        active_red4 += 1
        score += 1

        
    if red3.colliderect(ground) and not lose:
        rx3 = random.randint(0,800)
        red3.x = rx3
        red3.y = 0
        active_red4 += 1
        score += 1


    if active_red4 > 12 and not lose:
        red4.x += red_speed + 0.5
        

    if red4.x >= 800 and not lose:
        active_red4 = 0
        red4.x = -40
        score += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player.x > 0 and not lose:
        player.x -= vel_x

    if key[pygame.K_RIGHT] and player.x < 800 - player.height and not lose:
        player.x += vel_x

    if key[pygame.K_SPACE] and Jump is False and not lose:
        Jump = True

    if Jump and not lose:
        player.y -= vel_y
        vel_y -= 1

        if vel_y < -15 and not lose:
            Jump = False
            vel_y = 15

    score_text = FONT.render(f"Score: {round(score)}" , 1 , "white")
    screen.blit(score_text,(10,10))

    if player.colliderect(red) or player.colliderect(red2) or player.colliderect(red3) or player.colliderect(red4):
        lose = True


    
    if lose:
        lose_text = FONT.render(f"Game over" , 1 , "white")
        screen.blit(lose_text,(300,250))

    

    pygame.display.update()

pygame.quit()