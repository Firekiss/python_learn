import pygame, sys


pygame.init()

SIZE = width, height = 640, 960
RED = (255, 0, 0)

bg_music = pygame.mixer.music.load('./jntm.mp3')
des_font = pygame.font.Font('./my_font.ttf', 30)
text = des_font.render('G你太美', True, RED)

screen = pygame.display.set_mode(SIZE)
pygame.mixer.music.play(-1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (300, 300))
    pygame.display.flip()

