import pygame
pygame.init()
import time
screen = pygame.display.set_mode((600,600))

list_keys = [False,False,False,False]
rocket = pygame.image.load("rocket.png")
background = pygame.image.load("background.png")
rocket_x = 300
rocket_y = 300
font = pygame.font.SysFont("Arial", 30)
while rocket_y < 600:
    screen.blit(background,(0,0))
    screen.blit(rocket,(rocket_x,rocket_y))
    text = font.render("Press Arrow keys to move the rocket", True, (255,0,0))
    screen.blit(text,(200,500))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                list_keys[0] = True
            if event.key == pygame.K_RIGHT:
                list_keys[1] = True
            if event.key == pygame.K_UP:
                list_keys[2] = True
            if event.key == pygame.K_DOWN:
                list_keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                list_keys[0] = False
            if event.key == pygame.K_RIGHT:
                list_keys[1] = False
            if event.key == pygame.K_UP:
                list_keys[2] = False
            if event.key == pygame.K_DOWN:
                list_keys[3] = False
    if list_keys[0]:
        rocket_x = rocket_x - 1
    if list_keys[1]:
        rocket_x = rocket_x + 1
    if list_keys[2]:
        rocket_y = rocket_y - 1
    if list_keys[3]:
        rocket_y = rocket_y + 1
    rocket_y = rocket_y + 0.5
text = font.render("HA you lost", True, (255,0,0))
screen.blit(text,(250,300))
print("HA you lost")
pygame.display.update()
time.sleep(2)    