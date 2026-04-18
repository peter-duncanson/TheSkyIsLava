import pygame
import sys
pygame.init()

size = width, height = 320, 320
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
tree = pygame.image.load("assets/tree.png")
treerect = tree.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            break


    treerect = treerect.move(speed)
    if treerect.left < 0 or treerect.right > width:
        speed[0] *= -1
    if treerect.top < 0 or treerect.bottom > height:
        speed[1] *= -1

    screen.fill(black)
    screen.blit(tree, treerect)
    pygame.display.flip()

pygame.quit()
sys.exit()
