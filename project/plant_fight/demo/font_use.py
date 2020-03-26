import pygame, sys


pygame.init()

size = width, height = 500, 500
RED = pygame.Color(255, 0, 0)

# 获取所有的字体
fonts = pygame.font.get_fonts()

font = pygame.font.SysFont('arialunicodettf', 30)
text = font.render('你好 !!', True, RED)

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (20, 20))
    pygame.display.flip()
